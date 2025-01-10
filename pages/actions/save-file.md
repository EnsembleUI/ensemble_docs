# saveFile

The `saveFile` action saves media files (e.g., images) to the default media storage and documents to the default documents directory on Android and IOS. On the web, it downloads the file to the browser's default download folder.

### Properties

| Property  | Type   | Description                                   |
| :-------- | :----- | :-------------------------------------------- |
| source    | string | The source URL of the file     |
| blobData  | string | Blob data of the file in base64 string     |
| type      | string | Type of the file which are `image` or `document`. If type is `document` then the action will consider the source or blobData to be of document file and will save the file in the default device document folder.     |
| onSuccess | action | Execute an Action on successfully saving the file. |

**Example**

#### 1. For `blobData` input: ####
 In case the type is image, action will save image in default Pictures path of device, in case of web, it will download the file 
```yaml
Button:
  onTap:
     saveFile:
       fileName: 'Test.png'
       type: image
       blobData:  # blob string for image
```

 In case the type is document, action will save document in default Documents path of device, in case of web, it will download the file 
```yaml
In case the type is document, it'll be saved in Documents
Button:
  onTap:
     saveFile:
       fileName: 'Test.pdf'
       type: document # pdf, docx, txt
       blobData:  # blob string for document
```
#### 2. For `source` input: ####
```yaml
Button:
  onTap:
     saveFile:
       fileName: 'Test.pdf'
       type: document # pdf, docx, txt
       source: https://pdfobject.com/pdf/sample.pdf  # source-url for document
```
You can try complete example [here](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/9rgeMobpDsSosMoL2Hxv)
