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

## Latest list — 2026-10-23 06:20 UTC

New packages created between 2026-10-23 05:19 UTC and 2026-10-23 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T06-20-21-537757Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 05:31:37 | [RecursiveAI.OneImage.Psd](https://www.nuget.org/packages/RecursiveAI.OneImage.Psd) | 1.4.0 | Recursive AI, LLC | Photoshop PSD and PSB support for OneImage: reads the merged composite as an im… |
| 2026-10-23 05:32:49 | [IO3.__SERVICE_NAME__.Service.SDK](https://www.nuget.org/packages/IO3.__SERVICE_NAME__.Service.SDK) | 3.0.0 | IO3.__SERVICE_NAME__.Service.… | Package Description |
| 2026-10-23 05:35:07 | [Jtext103.CFET2.MQTTCommunicationModule](https://www.nuget.org/packages/Jtext103.CFET2.MQTTCommunicationModule) | 1.0.0 | Jtext103 | CFET2 MQTT event communication using an external broker; observation control is… |
| 2026-10-23 05:49:11 | [BeneficialStrategies.Iso20022.Messages](https://www.nuget.org/packages/BeneficialStrategies.Iso20022.Messages) | 1.0.0-alpha | Jeff Ward,Beneficial Strategi… | An interface for every ISO 20022 message, component and choice, with the verbat… |
| 2026-10-23 06:03:42 | [DWIS.RigOS.Contracts.DownholeMechanical](https://www.nuget.org/packages/DWIS.RigOS.Contracts.DownholeMechanical) | 1.0.0 | DWIS.RigOS.Contracts.Downhole… | Vendor-neutral distributed downhole mechanical measurements and equipment/posit… |
| 2026-10-23 06:05:15 | [DWIS.RigOS.DownholeMechanical.Bridge](https://www.nuget.org/packages/DWIS.RigOS.DownholeMechanical.Bridge) | 1.0.0 | DWIS.RigOS.DownholeMechanical… | Shared subscription-based downhole mechanical bridge runtime for DWIS providers. |
| 2026-10-23 06:06:58 | [FluentUI.Svg2Font.Tools](https://www.nuget.org/packages/FluentUI.Svg2Font.Tools) | 6.5.3 | ema | MSBuild props that expose pointing to the bundled svg2font.exe. Use it from Exe… |
| 2026-10-23 06:11:05 | [Teknosol.DataReconciler.Core](https://www.nuget.org/packages/Teknosol.DataReconciler.Core) | 1.0.1 | Teknosol.DataReconciler.Core | Cross-service replica reconciliation engine (scan, promote, heal, dedupe, daily… |
| 2026-10-23 06:12:31 | [Nexusq](https://www.nuget.org/packages/Nexusq) | 4.1.1 | lecodev-26 | Thin P/Invoke bindings over the NEXUS-Q C SDK (libnexusq): post-quantum vault,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
