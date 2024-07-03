
# Beem 2.0 - StartUp Link x Beem AI

##### [beemers-ai]
#### Beem 2.0 is an integrated solution that combines a payment app, spend analysis, expense tracking, and a blockchain-based helpdesk system. This project leverages multiple open-source repositories to provide a comprehensive platform for managing finances and resolving disputes.

### Key Components: 
1. **Payment App**: [Payflow](https://github.com/felipecastrosales/payflow) 
2. **Spend Analysis**: [Bahi-Khata](https://github.com/Bahi-Khata-App/Bahi-Khata) 
3. **Expense Tracking**: 
		- [Expenso](https://github.com/Spikeysanju/Expenso) 
		- [Zero](https://github.com/indranilbhuin/zero) 
4. **UPI Payments**: [GpayApp-Flutter](https://github.com/muhammad-fiaz/GpayApp-Flutter) 
5. **Receipt Scanning**: 
	   - [Receipt-Wrangler](https://github.com/Receipt-Wrangler) 
	   - [Expense-Tracker + OCR](https://github.com/shubham99bisht/Expense-Tracker) 
6. **Gift Card Generation**: [Bannerbear Guide](https://www.bannerbear.com/blog/how-to-auto-generate-unique-gift-cards-with-open-ai-and-bannerbear-nodejs/) 
7. **Blockchain Helpdesk**: 
       - [DigiByte JS](https://github.com/RenzoDD/digibyte-js) 
       - [Digi-ID Protocol](https://medium.com/geekculture/digi-id-a-blockchain-based-open-authentication-protocol-14f60446e39e)


### Payment App:
   - A payment and bills management app, key features include social login with Google, Firebase MLKit for QR code reading, camera usage, bill registerationwith details like ticket name, maturity data, price and QR code and the ability to query statements. Built with Flutter.
**Repository**: [Payflow](https://github.com/felipecastrosales/payflow)
   
### Spend Analysis:
   - It helps users manage their spendings by tracking expenses from various sources like Amazon, Flipkart, Myntra, Ola, Uber, Zomato, Swiggy, and Curefit. It uses Flask, Heroku, Gmail API, Beautiful Soup, and Altair to gather, analyze, and visualize spending data. Users can receive email reports summarizing their expenses.
**Repository**: [Bahi-Khata](https://github.com/Bahi-Khata-App/Bahi-Khata)

### Expense Tracker:
   - This is a minimal expense tracker app built with modern Android architecture components, following the MVVM (Model-View-ViewModel) pattern. It is developed using Kotlin and includes features such as tracking income and expenses, a detailed dashboard, transaction management, and dark mode support. The app uses Room for database management and integrates with Jetpack components like DataStore, StateFlow, and Navigation. The app's design is prototyped using Figma.
		1. **Repository**: [Expenso](https://github.com/Spikeysanju/Expenso)
		2. **Repository**: [Zero](https://github.com/indranilbhuin/zero)

### UPI Integration:
   - An open-source, lightweight expense management app built with MongoDB Realm, ensuring data privacy by storing data locally. Features include account creation, expense tracking, category management, debt tracking, analytics with insights and heatmaps, and customization options. The app offers a minimalistic UI, supports dark and light themes, and allows users to export/import data in JSON format.
**Repository**: [GpayApp-Flutter](https://github.com/muhammad-fiaz/GpayApp-Flutter)

### Receipt Scanning:
   - An easy-to-use self-hosted receipt manager featuring OCR/AI image scanning for receipt creation, smart categorization for filtering, and collaborative expense tracking. It supports multi-user functionality, email integration for uploading receipts, bulk uploads, and simple dashboards for managing and analyzing receipts. Future enhancements include a mobile app, YNAB integration, and continuous feature improvements.
**Repository**: [Receipt-Wrangler](https://github.com/Receipt-Wrangler)

   - This project focuses on key information extraction from scanned receipts, utilizing OCR technology to detect and extract text. It identifies key fields like store name, address, date, invoice ID, total amount, and items using a Bi-LSTM based approach. The app includes a GUI for labeling entities, a web interface for uploading and viewing results, and an Android UI for managing receipts.
 **Repository**: [Expense-Tracker + OCR](https://github.com/shubham99bisht/Expense-Tracker)

### Auto-Generating Unique Gift Cards:
   - This guide demonstrates using OpenAI and Bannerbear to create personalized gift cards. Bannerbear allows customization of image templates via API, and OpenAI's DALL·E generates unique images. The process involves setting up API keys, creating a project in Bannerbear, and using Node.js to automate image generation and gift card creation, including QR codes for redemption links.
**Guide**: [Bannerbear Blog](https://www.bannerbear.com/blog/how-to-auto-generate-unique-gift-cards-with-open-ai-and-bannerbear-nodejs/)

### Blockchain Helpdesk System:
   - A JavaScript library for the DigiByte blockchain, based on Bitcore Lib. It facilitates various DigiByte functionalities, including generating addresses, creating and signing transactions, verifying messages, and creating multisig addresses. The library supports both Node.js and browser environments, making it versatile for different development needs. 
  - Implements Digi-ID for a secure, password-less login experience. 
  - Explains the use of OP_RETURN fields and UTXO-based blockchains to store encrypted conflict tokens directly on the blockchain, creating a secure helpdesk system.
  **Article**: [Digi-ID: A Blockchain-Based Open Authentication Protocol](https://medium.com/geekculture/digi-id-a-blockchain-based-open-authentication-protocol-14f60446e39e)
  **Repository**: [DigiByte JS](https://github.com/RenzoDD/digibyte-js)    

## Setting Up Beem 2.0 
### Prerequisites 
- Ngrok 
- Node.js 
- Flutter SDK 
- Dart SDK
- Firebase
- OpenAI
- Access to a DigiByte node 

### Step-by-Step Guide
####  Clone the Repositories 
```bash 
git clone https://github.com/felipecastrosales/payflow 
git clone https://github.com/Bahi-Khata-App/Bahi-Khata 
git clone https://github.com/Spikeysanju/Expenso 
git clone https://github.com/indranilbhuin/zero 
git clone https://github.com/muhammad-fiaz/GpayApp-Flutter 
git clone https://github.com/Receipt-Wrangler 
git clone https://github.com/shubham99bisht/Expense-Tracker 
git clone https://github.com/RenzoDD/digibyte-js 
```

##### Due to timeframe constraints, we were not able to build the full function. These are the resources we found online that can be utilised in our payment solution, making it holistic and achievable.
