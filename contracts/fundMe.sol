// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract fundMe is ReentrancyGuard {
    AggregatorV3Interface internal priceFeed;
    address public owner;
    event OwnerSet(address indexed previousOwner, address indexed newOwner);
    event log(address sender, uint256 amount);

    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
        emit OwnerSet(address(0), owner);
    }

    address[] public funders;
    mapping(address => uint256) public addresstoamountFunded;

    function fundme() public payable {
        uint256 minPay = 50 * 10 ** 18;
        require(
            getConversionRate(msg.value) >= minPay,
            "You need to spend more ETH!"
        );
        addresstoamountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer) * 1e10;
    }

    function getConversionRate(
        uint256 ethAmount
    ) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 ethAmount_USD = (ethPrice * ethAmount) / 1e18;
        return ethAmount_USD;
    }

    function getEntranceFee() public view returns (uint256) {
        uint256 minPay = 51 * 10 ** 18;
        uint256 precision = 1 * 1e18;
        uint256 price = getPrice();
        uint256 entryFee = (minPay * precision) / price;
        return entryFee;
    }

    receive() external payable {
        emit log(msg.sender, msg.value);
    }

    fallback() external {}

    modifier onlyOwner() {
        require(owner == msg.sender, "Caller is not Owner");
        _;
    }

    function transferOWnership(address newOwner) public onlyOwner {
        emit OwnerSet(owner, newOwner);
        owner = newOwner;
    }

    function renounceOwnership() public onlyOwner {
        emit OwnerSet(owner, address(0));
        transferOWnership(address(0));
    }

    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
        uint8 i = 0;
        while (i < funders.length) {
            address funder = funders[i];
            addresstoamountFunded[funder] = 0;
            ++i;
        }
        funders = new address[](0);
    }
}
