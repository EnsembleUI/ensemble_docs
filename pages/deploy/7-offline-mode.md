# Making your app work when offline

You can embed your app definition in your build output so that your app works without network connectivity. Note that once you make this change, you will not have the ability to change the app from Ensemble Studio.

## Prerequisites

* You have completed the [Prepare your app for deployment step](/deploy/1-prepare-app).
* You have a text or code editor on your machine. We recommend [VS Code](https://code.visualstudio.com/).

## Step 1. Create a folder for your app

In your local directory where you cloned Ensemble Starter, navigate to `/ensemble/apps` folder. Create a new folder with your desired name, and no spaces.

This name will not be customer-facing.

<img src="/images/local_app_folder.png" alt="Local app folder" height="500"/>

## Step 2. Copy your app artifacts  

To work in local mode, you can obtain your app artifacts from either **Ensemble Studio** or the **Desktop app**. Once obtained, copy and paste the downloaded folders into the `/ensemble/apps` folder you created.  

The downloaded app will already have the following structure:  

```
<project-path>/
├── asset/
├── screen/
├── internal_widget/
├── internal_script/
├── theme/
├── i18n/
├── config/
├── secrets/
└── font/
```
#### Option 1: Downloading Artifacts from Ensemble Studio  

1. Open **Ensemble Studio**.  
2. Click the `...` menu button for your app.  
3. Select **Download Beta** to download all the app artifacts.  
4. Once downloaded, locate the app folder.  
5. Copy the entire folder (with the above structure).  
6. Paste the folder into the `/ensemble/apps` directory you created.  

#### Option 2: Obtaining Artifacts from the Desktop App  

To obtain local artifacts from the Desktop app, pull the app directly into the `/ensemble/apps` folder in your local directory where you cloned the Ensemble Starter.

Follow this [guide](/desktop-app/installation#pulling-from-cloud-to-local) to pull the app from the Desktop app.


## Step 4. Update your app to read the definitions locally

In your local directory where you cloned Ensemble Starter, open `/ensemble/ensemble-config.yaml` file with your desired code or text editor.

At the top, set the `from` property to `local`:

```yaml
definitions:
  # where your page definitions are hosted ('local', 'remote' or 'ensemble')
  from: local
```

Then set the `appId` and `appHome` properties under `local`

```yaml
  local:
    path: ensemble/apps/<your-app-name>
    appId: myApp   # this is the name of the folder you created in step 1
    appHome: MyHomeScreen # this is the name of the screens that should be rendered first when your app id launched
```
## Step 5. Update starter `pubspec.yaml`
Once you've placed your app artifacts into the `/ensemble/apps` folder, update the `pubspec.yaml` file in your starter project to include the paths for the assets.  

Add the following under the `assets` section:  

```yaml
flutter:
  assets:
    - ensemble/apps/<your-app-name>/
    - ensemble/apps/<your-app-name>/screen/
    - ensemble/apps/<your-app-name>/internal_widget/
    - ensemble/apps/<your-app-name>/internal_script/
    - ensemble/apps/<your-app-name>/asset/
    - ensemble/apps/<your-app-name>/i18n/
    - ensemble/apps/<your-app-name>/theme/
    - ensemble/apps/<your-app-name>/config/appConfig.json
    - ensemble/apps/<your-app-name>/secret/secrets.json
    - ensemble/apps/<your-app-name>/.manifest.json
```

### Important Note:  
You only need to include the folders or files in the `pubspec.yaml` file that are present in your app. For example:  
- If your app does not include a **theme**, do not add the `ensemble/apps/<your-app-name>/theme/` path.  
- Similarly, omit paths for any other folders or files that are not part of your app.  

This ensures that your app is properly configured and avoids unnecessary references to non-existent assets. Replace `<your-app-name>` with the actual name of your app folder.  
## 5. Rebuild your app

Now you can follow the steps for iOS or Android to run the app locally or build and upload your app to the respective app stores.
