
# Guide: Generating a Firebase Service Account for App Distribution

## Overview

This guide outlines the steps to generate a Firebase Service Account with the necessary permissions to use the Firebase App Distribution API for seamless app distribution.

---

## Steps for Creating a Firebase Service Account

### 1. Log in to Firebase Console

- Open the [Firebase Console](https://console.firebase.google.com/).
- Ensure you are logged in with the account associated with your Firebase project.

### 2. Navigate to Project Settings

- Select your project by clicking on its name in the top-left corner.
- From the dropdown menu, select **Project Settings**.
- Select the **Service accounts** tab
- Click the **X service accounts** button to open the Google Cloud Platform interface.

![Firebase Service Accounts Button](/images/deploy/firebase_service_accounts_button.png)

---

### 3. Create a New Service Account

#### a. Access Service Accounts

- In the Google Cloud Platform, navigate to the **Service Accounts** section.
- Click the **Create Service Account** button.

![Create Service Account Button](/images/deploy/service-account.png)

#### b. Fill in Service Account Details

- **Step 1**: Enter the Service Account name and description. This helps you identify the account later and click **Create**.
- **Step 2**: Click the **Select a role** dropdown and choose **Firebase App Distribution Admin** and Click **Continue**.
- **Step 3**: Leave additional fields blank and click **Done**.

---

### 4. Manage Service Account Keys

#### a. Locate Your Service Account

- In the list of service accounts, find the one you just created.
- Click the menu in the **Actions** column and select **Manage keys**.

![Manage Keys Button](/images/deploy/google_cloud_three.png)

#### b. Create a New Key

- In the **Keys** section, click **Add Key > Create new key**.
- Select **JSON** as the key type and click **Create**.
- Download the JSON key file and save it in a secure location.

![Download JSON Button](/images/deploy/google_cloud_four.png)

---

### 5. Upload the JSON Key to Ensemble Studio

- Return to Ensemble Studio.
- Upload the JSON key file to the **Firebase App Distribution** configuration in the **Build & Deploy** page.
