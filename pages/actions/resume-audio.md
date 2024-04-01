# resumeAudio

resumeAudio action allows users to resume a previously paused audio

### Properties

| Property | Type   | Description                                                                                                                    |
| :------- | :----- | :----------------------------------------------------------------------------------------------------------------------------- |
| id       | string | A unique identity that's required to refer to the audio that was paused in past. Should be same as that of passed in playAudio |

**Example**

```yaml
View:
  header:
    title: Audio Player
  styles:
    scrollableView: true

  body:
    Column:
      styles:
        gap: 16
        padding: 24
      children:
        - Button:
            label: Play Audio
            onTap:
              playAudio:
                id: My Audio
                source: "https://file-examples.com/storage/fe8119f4e865f33329898be/2017/11/file_example_MP3_700KB.mp3"
                volume: 1 # 0 to 1
                balance: 0 # -1 to 1
                position: 2 # in seconds
                onComplete:
                  executeCode:
                    body: |
                      console.log("Audio Played");

        - Button:
            label: Play Audio 2
            onTap:
              playAudio:
                id: My Audio
                source: audio.mp3
                volume: 1 # 0 to 1
                balance: 0 # -1 to 1
                position: 2 # in seconds
                onComplete:
                  executeCode:
                    body: |
                      console.log("Audio Played");

        - Button:
            label: Pause Audio
            onTap:
              pauseAudio:
                id: My Audio

        - Button:
            label: Stop Audio
            onTap:
              stopAudio:
                id: My Audio

        - Button:
            label: Resume Audio
            onTap:
              resumeAudio:
                id: My Audio

        - Button:
            label: Seek Audio at 4 second
            onTap:
              seekAudio:
                id: My Audio
                position: 20 # in seconds
```
