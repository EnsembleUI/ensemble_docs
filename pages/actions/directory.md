# Actions

When an event is triggered (e.g. button is tapped), you can perform actions such as navigate to a screen, call an API, or even run JavaScript code.

### Backend API interaction

| Property                   | Description                                                                                                 |
| :------------------------- | :---------------------------------------------------------------------------------------------------------- |
| [invokeAPI](invoke-API.md) | invokeAPI is used for calling an API. You can call an API on events such as a button tap or on screen load. |

### Navigation & UI transitions

| Property                                        | Description                                                                                                                                                                   |
| :---------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [navigateScreen](navigate-screen.md)            | navigateScreen action facilitates smooth navigation to a specific screen or page within the app's interface.                                                                  |
| [navigateModalScreen](navigate-modal-screen.md) | navigateModalScreen action opens a specific screen or page as a modal overlay, focusing on the temporary view without losing the main app context.                            |
| [navigateViewGroup](navigate-view-group.md)     | navigateViewGroup action allows users to navigate between menu items while maintaining the menu in place. This simulate the experience when user taps on different nav items. |
| [navigateBack](navigate-back.md)                | navigateBack action allows users to go back to the previous screen or page within the app's navigation stack.                                                                 |
| [onViewGroupResume](onViewGroupResume.md)            | onViewGroupResume action facilitates ensembleAction execution when navigating back to ViewGroup from different screen.                                                                  |
| [onViewGroupUpdate](onViewGroupUpdate.md)            | onViewGroupUpdate action facilitates ensembleAction execution when update in ViewGroup occurs such as swithcing screen.                                                                  |
| [showDialog](show-dialog.md)                    | showDialog action triggers the display of a modal dialog box within the app, presenting important information or notifications.                                               |
| [closeAllDialogs](close-all-dialogs.md)         | closeAllDialogs action dismisses or closes all open modal dialogs within the app, ensuring a clutter-free interface.                                                          |
| [showToast](show-toast.md)                      | showToast action displays a temporary notification or message on the app interface, providing concise and contextual updates to users.                                        |
| [uploadFiles](upload-files.md)                  | uploadFiles action allows users to select and upload files from their device to the app, facilitating data transfer and sharing.                                              |

### Device capabilities

| Property                                                    | Description                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [openCamera](open-camera.md)                                | openCamera action allows users to access their device's camera within the app for capturing images and videos.                                                                                                                                                                                                |
| [getLocation](get-location.md)                              | getLocation action retrieves the device's current location, enabling location-based functionalities within the app.                                                                                                                                                                                           |
| [requestNotificationAccess](request-notification-access.md) | requestNotificationAccess action prompts users to grant permission for the app to send notifications to their device.                                                                                                                                                                                         |
| [showNotification](show-notification.md)                    | showNotification action displays local notifications within the app, notifying users of important events or information.                                                                                                                                                                                      |
| [notification](notification.md)                             | notification action manages and handles notifications within the app, enabling effective communication with users and delivering timely updates and alerts.                                                                                                                                                   |
| [pickFiles](pick-files.md)                                  | pickFiles action enables users to select files from their device for further processing or usage within the app.                                                                                                                                                                                              |
| [uploadFiles](upload-files.md)                              | uploadFiles action allows users to select and upload files from their device to the app, facilitating data transfer and sharing.                                                                                                                                                                              |
| [getNetworkInfo](get-network-info.md)                       | enables users to retrieve their device's current location, facilitating location-based functionalities within the app, such as mapping, navigation, or personalized content delivery, enhancing user experience and context-aware interactions. It requests user's permission to get his/her current location |
| [saveFile](save-file.md)                                    | The saveFile action saves media files (e.g., images) to the default media storage and documents to the default documents directory on Android and IOS. On the web, it downloads the file to the browser's default download folder.                                                                            |

### Secure Storage

| Property                                      | Description                                                                                                                                          |
| :-------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| [setSecureStorage](set-secure-storage.md)     | setSecureStorage action securely stores sensitive information in an encrypted format on the device, ensuring that sensitive data remains protected.  |
| [getSecureStorage](get-secure-storage.md)     | getSecureStorage action retrieves previously stored encrypted data from the device's secure storage, decrypting it for use within your application.  |
| [clearSecureStorage](clear-secure-storage.md) | clearSecureStorage action removes previously stored encrypted data from the device's secure storage, allowing you to clean up sensitive information. |
| [saveKeychain](save-keychain.md)              | saveKeychain action stores sensitive information in the device's secure keychain (iOS) and keyStore (Android).                                       |
| [readKeychain](read-keychain.md)              | readKeychain action retrieves previously stored data from the device's secure keychain (iOS) and keyStore (Android).                                 |
| [clearKeychain](clear-keychain.md)            | clearKeychain action removes previously stored data from the device's secure keychain (iOS) and keyStore (Android).                                  |

### Other interactions

| Property                                | Description                                                                                                                                    |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| [executeCode](execute-code.md)          | executeCode action executes custom code logic within the app, enabling dynamic functionality and personalized interactions.                    |
| [openUrl](open-url.md)                  | openUrl action opens external URLs or web links within the app, facilitating seamless integration with external content.                       |
| [startTimer](start-timer.md)            | startTimer action initiates a timer within the app, facilitating time-sensitive processes and triggering events after a specified duration.    |
| [openUrl](open-url.md)                  | openUrl action allows users to open external URLs or web links within the app, enhancing content integration.                                  |
| [stopTimer](stop-timer.md)              | stopTimer action halts or pauses a running timer within the app, providing control over time-sensitive processes.                              |
| [copyToClipboard](copy-to-clipboard.md) | copyToClipboard action copies text or content to the device's clipboard, facilitating easy sharing and transfer of information within the app. |

### 3-rd party services

| Property                            | Description                                                                                                                                           |
| :---------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [connectWallet](connect-wallet.md)  | connectWallet action establishes a connection between the app and the user's digital wallet, enabling blockchain-based interactions and transactions. |
| [openPlaidLink](open-plaid-link.md) | Open the Plaid Link Service so user can link their financial accounts to your service.                                                                |

### Audio Player

| Property                       | Description                                                                      |
| :----------------------------- | :------------------------------------------------------------------------------- |
| [playAudio](play-audio.md)     | The playAudio action allows users to play a given audio file from a URL or asset |
| [pauseAudio](pause-audio.md)   | The pauseAudio action allows users to pause an already-playing audio file        |
| [resumeAudio](resume-audio.md) | The resumeAudio action allows users to resume a previously paused audio          |
| [stopAudio](stop-audio.md)     | The stopAudio action allows users to stop a already playing audio file           |
| [seekAudio](seek-audio.md)     | The seekAudio action allows users to pause a already-playing audio file          |
