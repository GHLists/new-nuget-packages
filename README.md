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

## Latest list — 2026-10-22 22:22 UTC

New packages created between 2026-10-22 21:19 UTC and 2026-10-22 22:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T22-22-22-256745Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 21:24:52 | [SpCraft.Net.Common.Http.Correlation](https://www.nuget.org/packages/SpCraft.Net.Common.Http.Correlation) | 2.0.42 | SpCraft.Net.Common.Http.Corre… | Package Description |
| 2026-10-22 21:31:38 | [RecursiveAI.OneImage.Text](https://www.nuget.org/packages/RecursiveAI.OneImage.Text) | 1.2.0 | Recursive AI, LLC | Fonts and text for OneImage: loads TrueType, OpenType (CFF), TrueType Collectio… |
| 2026-10-22 21:35:23 | [EzeIO.Keylogger](https://www.nuget.org/packages/EzeIO.Keylogger) | 1.1.0 | Eze-IO | A library that uses the Windows low-level keyboard hook (WH_KEYBOARD_LL) to rai… |
| 2026-10-22 21:43:51 | [Sakura.Framework.Android](https://www.nuget.org/packages/Sakura.Framework.Android) | 2026.1023.0 | HelloYeew | Runs a Sakura Framework app on Android: the activity, window, touch, lifecycle… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
