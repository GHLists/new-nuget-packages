# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 23:19 UTC

New packages created between 2026-11-10 22:21 UTC and 2026-11-10 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T23-19-02-936586Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 22:53:25 | [YawVR.Link](https://www.nuget.org/packages/YawVR.Link) | 1.0.0 | YawVR.Link | Build YawVR-compatible motion simulator emulators and senders without touching… |
| 2026-11-10 22:56:27 | [Tessaro.Results](https://www.nuget.org/packages/Tessaro.Results) | 0.1.0 | Igor Tessaro | A zero-dependency result type for .NET: return success or categorised errors in… |
| 2026-11-10 23:04:51 | [NuBouncer](https://www.nuget.org/packages/NuBouncer) | 0.1.0 | Marcus Smallman-Lewis | Stops AI coding agents adding NuGet packages that don't exist or look dodgy. Ch… |
| 2026-11-10 23:11:38 | [VIEApps.Components.Utility.Image.StrongName](https://www.nuget.org/packages/VIEApps.Components.Utility.Image.StrongName) | 10.11.2611.1 | VIEApps.net | The tiny library to help .NET apps working with image (include captcha image) i… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
