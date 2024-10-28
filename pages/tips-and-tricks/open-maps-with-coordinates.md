# Open Maps with Coordinates on Android and iOS

This guide explains how to open map applications with specific coordinates on Android and iOS devices. The examples demonstrate how to launch Google Maps or Apple Maps, depending on the platform, and also include the ability to use dynamic coordinates input.

[Test in Kitchen Sink](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/wCU2q0PQnNxmXqN4WyCV)

## Implementation Overview

The feature allows users to open their default map application (Google Maps or Apple Maps) with specific coordinates by clicking an icon. Depending on the user's device (Android, iOS, or Web), the appropriate map service will be launched. Additionally, users can enter dynamic coordinates to open any location.

### Examples

### Example 1: Open Google Maps with Static Coordinates

This example demonstrates how to open a specific location in Google Maps using a simple icon click.

**Sample Coordinates:**  
- Latitude: `38.7946`
- Longitude: `106.5348`

#### UI Layout:

```yaml
View:
  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
          - Text: Click on the icon to open location on Google Maps
          - Row:
              styles:
                gap: 8
                crossAxis: center
              children:
                - Text:
                    text: "Sample Location: 38.7946,106.5348"
                    styles:
                      textStyle:
                        fontSize: 14
                - Icon:
                    name: locationArrow
                    library: fontAwesome
                    color: blue
                    size: 18
                    onTap:
                      openUrl:
                        url: https://www.google.com/maps/?q=38.7946,106.5348(Ensemble+Technologies)
```

#### Action Output Screenshot:

<div style="display: flex; flex-direction: column; align-items: center; margin-top: 10px;">
<img src="/images/tips/google_map.jpg" style="text-align: center;" alt="Output Screenshot" width="250"/>
  <p>Clicking the icon will open Google Maps with the provided coordinates and label.</p>
</div>



### Example 2: Open Apple Maps with Static Coordinates

This example demonstrates how to open a specific location in Apple Maps.

#### UI Layout:

```yaml
View:
  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
         - Text: Click on the icon to open location on Apple Maps
         - Row:
            styles:
              gap: 8
              crossAxis: center
            children:
              - Text:
                  text: "Sample Location: 38.7946,106.5348"
                  styles:
                    textStyle:
                      fontSize: 14
                      fontWeight: w300
              - Icon:
                  name: locationArrow
                  library: fontAwesome
                  color: blue
                  size: 18
                  onTap:
                    openUrl:
                      url: https://maps.apple.com/?ll=38.7946,106.5348&q=Ensemble+Technologies
```
#### Action Output Screenshot:

<div style="display: flex; flex-direction: column; align-items: center; margin-top: 10px;">
  <img src="/images/tips/apple_maps.png" style="text-align: center;" alt="Output Screenshot" width="250"/>
  <p>Clicking the icon will open Apple Maps with the provided coordinates and label.</p>
</div>


### Example 3: Open Map Application Based on Device

This example shows how to conditionally open the map application based on the user's device (Android, iOS, or Web).

#### UI Layout:

```yaml
View:
  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
         -  Text: Click on the icon to open location based on device. (Apple Maps on iPhone, Google Maps on Android)
         -  Row:
              styles:
                gap: 8
                crossAxis: center
              children:
                - Text:
                    text: "Sample Location: 38.7946,106.5348"
                    styles:
                      textStyle:
                        fontSize: 14
                        fontWeight: w300
                - Icon:
                    name: locationArrow
                    library: fontAwesome
                    color: blue
                    size: 18
                    onTap:
                      executeConditionalAction:
                        conditions:
                          - if: ${device.platform == "ios"}
                            action:
                              openUrl:
                                url: https://maps.apple.com/?ll=38.7946,106.5348&q=Ensemble+Technologies
                          - elseif: ${device.platform == 'android'}
                            action:
                              openUrl:
                                url: https://www.google.com/maps/?q=38.7946,106.5348(Ensemble+Technologies)
                          - elseif: ${device.platform == 'web'}
                            action:
                              openUrl:
                                url: https://www.google.com/maps/?q=38.7946,106.5348(Ensemble+Technologies)
```
#### Action Output Screenshot:
<div style="display: flex; align-items: center; justify-content: center; margin-top: 10px; gap: 20px ">
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img src="/images/tips/dynamic_google_map.jpg" style="text-align: center;" alt="Output Screenshot" width="250"/>
      <p>Output on Android</p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img src="/images/tips/dynamic_apple_map.png" style="text-align: center;" alt="Output Screenshot" width="250"/>
      <p>Output on Iphone</p>
    </div>
</div>

### Example 4: Dynamic Coordinates Input

In this example, users can input their own coordinates and label, which will dynamically open the respective map application based on the user's device.

#### UI Layout:

```yaml
View:
  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
         -  TextInput:
              label: Enter comma-separated Latitude and Longitude
              id: mapsCoordinates
         -  TextInput:
              label: Enter Label
              id: mapslabel
         -  Text: Click on the icon to open location based on device. (Apple Maps on iPhone, Google Maps on Android)
         -  Row:
              styles:
                gap: 8
                crossAxis: center
              children:
                - Text:
                    text: "Sample Location: 38.7946,106.5348"
                    styles:
                      textStyle:
                        fontSize: 14
                        fontWeight: w300
                - Icon:
                    name: locationArrow
                    library: fontAwesome
                    color: blue
                    size: 18
                    onTap:
                      executeConditionalAction:
                        conditions:
                          - if: ${device.platform == "ios"}
                            action:
                              openUrl:
                                url: https://maps.apple.com/?ll=${mapsCoordinates.value}&q=${mapslabel.value}
                          - elseif: ${device.platform == 'android'}
                            action:
                              openUrl:
                                url: https://www.google.com/maps/?q=${mapsCoordinates.value}(${mapslabel.value})
                          - elseif: ${device.platform == 'web'}
                            action:
                              openUrl:
                                url: https://www.google.com/maps/?q=${mapsCoordinates.value}(${mapslabel.value})
```