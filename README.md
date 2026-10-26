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

## Latest list — 2026-10-26 12:20 UTC

New packages created between 2026-10-26 11:20 UTC and 2026-10-26 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T12-20-25-114907Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 11:31:44 | [OnTheFlySettings.AzureFunctions](https://www.nuget.org/packages/OnTheFlySettings.AzureFunctions) | 1.0.0 | Shantanu | Azure Function Client for OnTheFlySettings endpoints. Fully automate the update… |
| 2026-10-26 11:53:36 | [Ashla.CombatLog](https://www.nuget.org/packages/Ashla.CombatLog) | 1.0.0 | YozoraCho and Ashla contribut… | Parses Star Wars: The Old Republic combat-log lines into Ashla.SDK combat event… |
| 2026-10-26 11:53:38 | [Ashla.SDK](https://www.nuget.org/packages/Ashla.SDK) | 1.0.0 | YozoraCho and Ashla contribut… | Build plugins for Ashla, the external overlay and combat-log framework for Star… |
| 2026-10-26 11:53:39 | [Ashla.UI](https://www.nuget.org/packages/Ashla.UI) | 1.0.0 | YozoraCho and Ashla contribut… | Optional UI kit for Ashla plugins that draw with Dear ImGui: Ashla's themes and… |
| 2026-10-26 11:58:17 | [Sdcb.Arithmetic.Mpdec](https://www.nuget.org/packages/Sdcb.Arithmetic.Mpdec) | 4.0.1 | sdcb | Raw low-level P/Invoke binding for libmpdec (mpdecimal), the arbitrary-precisio… |
| 2026-10-26 11:58:50 | [Sdcb.Arithmetic.Mpdec.runtime.linux-x64](https://www.nuget.org/packages/Sdcb.Arithmetic.Mpdec.runtime.linux-x64) | 4.0.1 | sdcb | Native libmpdec and libmpdec++ (mpdecimal 4.0.1, https://www.bytereef.org/mpdec… |
| 2026-10-26 11:59:02 | [Sdcb.Arithmetic.Mpdec.runtime.win-x64](https://www.nuget.org/packages/Sdcb.Arithmetic.Mpdec.runtime.win-x64) | 4.0.1 | sdcb | Native libmpdec and libmpdec++ (mpdecimal 4.0.1, https://www.bytereef.org/mpdec… |
| 2026-10-26 12:01:37 | [Arc56.Generated.HashMapsData2Value.zebgen-wallet](https://www.nuget.org/packages/Arc56.Generated.HashMapsData2Value.zebgen-wallet) | 1.0.1.2026102611 | HashMapsData2Value | Generated ARC-56 Algorand smart-contract clients for HashMapsData2Value/zebgen-… |
| 2026-10-26 12:09:32 | [ProTest.Avalonia.Headless.XUnit.v4](https://www.nuget.org/packages/ProTest.Avalonia.Headless.XUnit.v4) | 12.1.4 | Wiesław Šoltés,Avalonia Team | Avalonia headless UI testing integration for xUnit.net 4.x (xunit.v3 packages). |
| 2026-10-26 12:09:32 | [ProTest.Avalonia.Headless](https://www.nuget.org/packages/ProTest.Avalonia.Headless) | 12.1.4 | Wiesław Šoltés,Avalonia Team | Avalonia headless platform, test sessions, input and gesture simulation, tree i… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
