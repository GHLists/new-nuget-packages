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

## Latest list — 2026-11-17 04:18 UTC

New packages created between 2026-11-17 03:19 UTC and 2026-11-17 04:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T04-18-39-987865Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 03:38:49 | [Cornhsu.XamlKeys](https://www.nuget.org/packages/Cornhsu.XamlKeys) | 0.1.0 | 許彧銘 (Cornhsu) | XamlKeys — static scope audit for XAML resource keys in WPF, WinUI, Avalonia an… |
| 2026-11-17 03:48:05 | [AlibabaCloud.SDK.QwenEduAiSuite20261102](https://www.nuget.org/packages/AlibabaCloud.SDK.QwenEduAiSuite20261102) | 1.0.0 | Alibaba Cloud | Alibaba Cloud QwenEduAiSuite (20261102) SDK Library for .NET |
| 2026-11-17 04:00:12 | [YarnSpinner.Shared](https://www.nuget.org/packages/YarnSpinner.Shared) | 3.3.0.5 | YarnSpinner.Shared | Package Description |
| 2026-11-17 04:00:15 | [JYPPX.ROCm.HIP.CSharp.API.Runtime.win-x64](https://www.nuget.org/packages/JYPPX.ROCm.HIP.CSharp.API.Runtime.win-x64) | 10.1.0 | JYPPX | Official AMD HIP and HIPRTC user-mode closure. Host AMD driver required. |
| 2026-11-17 04:00:35 | [YarnSpinner.HostAnalysis](https://www.nuget.org/packages/YarnSpinner.HostAnalysis) | 3.3.0.5 | YarnSpinner.HostAnalysis | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
