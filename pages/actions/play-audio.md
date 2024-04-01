# playAudio

playAudio action allows users to play a given audio file either from url or from assets. It requires a unique id passed to it so that the audio can be referrenced in future. It has parameters like `source`, `volumne`, `balance` and `position`.

### Properties

| Property  | Type   | Description                                              |
| :-------- | :----- | :------------------------------------------------------- |
| id | string | A unique identity that's required to refer to the given audio in the future |
| source | string | The source of the audio file. Can be a file name located in assets or can also be a url |
| volume | double | The volume at which audio to play. It should be between `0` and `1` with `0` being no volume and `1` being maximum volume. The default value is `1` |
| balance | double | The balance between both the left and right speakers for stereo audio. It should be between `-1` and `1` with `-1` being completely left speaker and `1` being completely right speaker. The default value is `0` |
| position | integer | The time stamp from which to play audio from. It should be in seconds. The default value is `0` |

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

**Related Actions: [pause-audio](pause-audio.md) [stop-audio](stop-audio.md) [resume-audio](resume-audio.md) [seek-audio](seek-audio.md)**

