# Ensemble Web Studio Documentation

## Installation & Setup

You can install Ensemble Web Studio directly using the appropriate installer for your operating system:

### Windows
1. Download the Windows installer [here](https://firebasestorage.googleapis.com/v0/b/ensemble-web-studio.appspot.com/o/desktop_app%2F0_1_0%2Fensemble-web-studio-0.1.0.Setup.exe?alt=media):
   ```
   https://firebasestorage.googleapis.com/v0/b/ensemble-web-studio.appspot.com/o/desktop_app%2F0_1_0%2Fensemble-web-studio-0.1.0.Setup.exe?alt=media
   ```
2. Run the downloaded `.exe` file
3. Launch Ensemble Web Studio

### macOS
1. Download the macOS package [here](https://firebasestorage.googleapis.com/v0/b/ensemble-web-studio.appspot.com/o/desktop_app%2F0_1_0%2Fensemble-web-studio-darwin-arm64-0.1.0.zip?alt=media):
   ```
   https://firebasestorage.googleapis.com/v0/b/ensemble-web-studio.appspot.com/o/desktop_app%2F0_1_0%2Fensemble-web-studio-darwin-arm64-0.1.0.zip?alt=media
   ```
2. Extract the downloaded `.zip` file
3. Move the application to your Applications folder
4. Launch Ensemble Web Studio

## Environment Modes

You can switch between Local and Development modes using the environment dropdown available on **home and every app page**:

### Development Mode

Development mode connects to the cloud environment:

- Files are stored in Firebase
- Requires internet connection
- Changes are synchronized with other collaborators
- Suitable for team collaboration

### Local Mode

Local mode allows you to work completely offline with files stored on your local machine:

- Files are stored in your system's user directory
- No internet connection required
- Changes are saved locally
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
2. Right-click on the app card you want to work with
3. Select "Pull App" from the context menu
4. Wait for the pull to complete

### Pushing Local Changes to Cloud

To push your local changes back to the cloud:
1. Launch the desktop application
2. Right-click on the app card
3. Select "Push App" from the context menu
4. Wait for your changes to push on the cloud

## Local File Structure

When working in local mode, files are organized as follows:

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

Key location:
- `metadata.json`: App configuration and settings

## Additional Resources

For more information or support, join the [Discord community](https://discord.gg/cEHkJTmn75) or refer to the official documentation.