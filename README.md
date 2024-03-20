# Brownie FundMe Project

Welcome to the Brownie FundMe project! This project involves the creation of fundme and withdrawal functions within the `FundMe` contract using Solidity. It also includes deploying the contract to various test networks using Python3, making testing and development a breeze.

## Features:
- **FundMe Contract:** Create fundme and withdrawal functions using Solidity for seamless interaction.
- **Deployment Flexibility:** Easily deploy contracts to various test networks including:
  - Mainnet-fork (Infura)
  - Mainnet-fork-dev (Alchemy)
  - Ganache-local (GUI - persistent development)
  - Brownie Ganache (development)
- **Funding and Withdrawing:** Interact with deployed contracts for funding and withdrawing effortlessly.
- **Testing Suite:** Comprehensive testing of fund and withdrawal functions using Brownie test framework.

## Getting Started:

1. **Clone Repository:** Clone this repository to your local machine.
2. **Install Dependencies:** Ensure you have Python3 installed and install necessary dependencies using `pip install -r requirements.txt`.
3. **Configure Networks:** Set up your preferred networks for deployment in the Brownie configuration.
4. **Deploy Contracts:** Use Brownie to deploy the contracts to your desired test networks.
5. **Interact and Test:** Fund and withdraw from the deployed contracts and run tests using Brownie.

## Deployment:
To deploy the contract to your preferred network, follow these steps:

```bash
brownie run deploy --network <network_name>
```

Replace `<network_name>` with the name of the network you wish to deploy to.

## Testing:
To run tests for fund and withdrawal functions:

```bash
brownie test
```

## Contribution:
Contributions are welcome! Feel free to open issues or pull requests for any improvements or features you'd like to see added.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** For detailed instructions and documentation, please refer to the [Wiki](wiki) section of this repository. Happy coding! 🚀
