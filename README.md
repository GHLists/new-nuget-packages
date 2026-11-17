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

## Latest list — 2026-11-17 23:19 UTC

New packages created between 2026-11-17 22:22 UTC and 2026-11-17 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T23-19-41-518176Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 22:25:12 | [DeveloperWorkspace.Templates](https://www.nuget.org/packages/DeveloperWorkspace.Templates) | 0.1.4 | Roger Hembury | Project templates for creating a Git-tracked developer workspace for AI prompts… |
| 2026-11-17 22:29:24 | [GoldMeridian.NativeAssets](https://www.nuget.org/packages/GoldMeridian.NativeAssets) | 1.0.0 | tomat | Enables referencing native libraries from package references for automatic, RID… |
| 2026-11-17 22:39:02 | [Refractor](https://www.nuget.org/packages/Refractor) | 0.1.0 | Quin Gillespie | Speech, braille and screen reader output for .NET through prism: NVDA, JAWS, SA… |
| 2026-11-17 22:42:22 | [StellarDrivePonder](https://www.nuget.org/packages/StellarDrivePonder) | 1.0.0 | StriderDev | Animated, client-local part guides for StellarDrive. |
| 2026-11-17 22:45:13 | [Anarchy.Toolkit.Web.MockServer.Ui](https://www.nuget.org/packages/Anarchy.Toolkit.Web.MockServer.Ui) | 1.0.0 | Leandro Melão Medeiros | Browser UI for Anarchy.Toolkit.Web.MockServer, built on Anarchy.Toolkit.Web.Ui:… |
| 2026-11-17 22:52:25 | [ViShap.Rewind.Core](https://www.nuget.org/packages/ViShap.Rewind.Core) | 1.0.0 | Vahe Babayan (0xVahe) | The engine of ViShap.Rewind: scopes that make a block of code an atomic unit of… |
| 2026-11-17 22:52:27 | [ViShap.Rewind.Generator](https://www.nuget.org/packages/ViShap.Rewind.Generator) | 1.0.0 | Vahe Babayan (0xVahe) | The source generator and analyzers of ViShap.Rewind. They run in the compiler;… |
| 2026-11-17 22:52:28 | [ViShap.Rewind.Testing](https://www.nuget.org/packages/ViShap.Rewind.Testing) | 1.0.0 | Vahe Babayan (0xVahe) | Test tools for code that uses ViShap.Rewind: proves that every failure point of… |
| 2026-11-17 22:52:29 | [ViShap.Rewind](https://www.nuget.org/packages/ViShap.Rewind) | 1.0.0 | Vahe Babayan (0xVahe) | Atomic in-memory state change for .NET: a block of code either keeps all its ch… |
| 2026-11-17 23:02:44 | [Sharpfy.Nextapi](https://www.nuget.org/packages/Sharpfy.Nextapi) | 0.2.0 | Sharpfy | SDK oficial da NextAPI para .NET: CNPJ (inclusive alfanumérico), CEP, sócios e… |
| 2026-11-17 23:11:39 | [TensorStack.AudioCpp](https://www.nuget.org/packages/TensorStack.AudioCpp) | 0.14.14 | sa_ddam213 | .NET Wrapper API for audio.cpp |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
