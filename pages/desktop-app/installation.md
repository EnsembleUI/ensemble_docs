# Ensemble Studio Desktop App

## When to use the desktop app

1. If you wish to use your own git to store your app definition - this allows you to create branches and pull requests.
2. If you wish to work offline and without internet connection

## Installation & Setup

### Windows

1. Download the Windows installer [here](https://firebasestorage.googleapis.com/v0/b/ensemble-web-studio.appspot.com/o/desktop_app%2Fensemble-web-studio-0.1.0%20Setup.exe?alt=media):

2. Run the downloaded `.exe` file
3. Launch Ensemble Web Studio
4. **Note:** Microsoft Defender SmartScreen may display a warning
Step 1: You will see a "Windows protected your PC" message.
Step 2: Click "More info" text to reveal additional options.
Step 3: Click "Run anyway" button to proceed with the installation.
Once confirmed, the application will open.

### MacOS

1. Download the macOS package [here](https://firebasestorage.googleapis.com/v0/b/ensemble-web-studio.appspot.com/o/desktop_app%2Fensemble-web-studio-darwin-arm64-0.1.0.zip?alt=media):
2. Extract the downloaded `.zip` file
3. Move the application to your Applications folder
4. **Note:** Until signing and notarizing is configured, you need to clear extended attributes for the app before launching it for the first time. Run the following command in the terminal:

   ```bash
   xattr -c <path_to_ensemble_app>
   ```

   Replace <path_to_ensemble_app> with the full path to the Ensemble Web Studio application. *This step is only required during the initial launch.*
5. Launch Ensemble Studio

## Environment Modes

You can switch between Local and Development modes using the environment dropdown available on **home and every app page**:

### Development Mode

Development mode connects to the cloud environment:

- Files are stored in Firebase
- Requires internet connection
- Changes are synchronized with other collaborators
- Suitable for real-time collaboration

### Local Mode

Local mode allows you to work completely offline with files stored on your local machine:

- Files are stored in your system's user directory
- No internet connection required
- Changes are saved locally
- Connect the local folder to a git provider to create branches and pull requests
- Perfect for offline development or testing

Local files location by operating system:

- Windows: `%APPDATA%/ensemble-web-studio`
- macOS: `~/Library/Application Support/ensemble-web-studio`

Note:

- You can switch between modes at any time using the dropdown
- The selected mode affects where your changes are saved
- Each mode maintains its own version of the files
- Remember to use Pull/Push operations when you want to sync between modes

## Synchronization

### Pulling from Cloud to Local

To work with an app locally:

1. Launch the desktop application
2. Click on the `...` menu button on the app card you want to work with
3. Select "Pull App" from the context menu
4. Select the target directory and click the `Pull` Button
5. Wait for the pull to complete

### Pushing Local Changes to Cloud

To push your local changes back to the cloud:

1. Launch the desktop application
2. Click on the `...` menu button on the app card you want to work with
3. Select "Push App" from the context menu
4. Wait for your changes to push on the cloud

## Local File Structure

When working in local mode, files are organized as follows:

```directory
<project-path>/
├── assets/
├── fonts/
├── scripts/
├── widgets/
├── screens/
├── translations/
├── config/
│   ├── appConfig.json
│   ├── secrets.json
├── theme.yaml
├── .manifest.json
```

Key location:

- `metadata.json`: App configuration and settings

## Additional Resources

For more information or support, join the [Discord community](https://discord.gg/cEHkJTmn75) or refer to the official documentation.
