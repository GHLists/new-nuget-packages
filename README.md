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

## Latest list — 2026-11-08 17:19 UTC

New packages created between 2026-11-08 16:19 UTC and 2026-11-08 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T17-19-31-857958Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 16:20:48 | [GM.FileStorage.Catalog](https://www.nuget.org/packages/GM.FileStorage.Catalog) | 4.1.0 | Giorgi Metskhvarishvili | Workflows for keeping GM.FileStorage files in your database: deleting the bytes… |
| 2026-11-08 16:31:22 | [Forge.Next.LocalWebShell](https://www.nuget.org/packages/Forge.Next.LocalWebShell) | 1.0.0 | Zoltan Juhasz | Runs an ASP.NET Core app (for example Blazor Server) as a local tool in the use… |
| 2026-11-08 16:38:51 | [perugius-core-contracts](https://www.nuget.org/packages/perugius-core-contracts) | 1.0.0 | core-contracts | Package Description |
| 2026-11-08 16:56:45 | [AdaskoTheBeAsT.Typewriter.CodeModel](https://www.nuget.org/packages/AdaskoTheBeAsT.Typewriter.CodeModel) | 4.16.0 | AdaskoTheBeAsT | CodeModel contracts, configuration, and helper extensions for Typewriter .tst t… |
| 2026-11-08 17:04:12 | [MMCA.Common.Passkeys](https://www.nuget.org/packages/MMCA.Common.Passkeys) | 1.281.0 | Ivan Ball | MMCA framework: opt-in passkey (WebAuthn) sign-in and second factor. Verifies r… |
| 2026-11-08 17:05:29 | [NumSharp.Interop.MLNet](https://www.nuget.org/packages/NumSharp.Interop.MLNet) | 0.80.0 | Eli Belash, Haiping Chen, Mei… | Interop between NumSharp NDArray and ML.NET (Microsoft.ML) data. Expose an NDAr… |
| 2026-11-08 17:05:31 | [NumSharp.Interop.OnnxRuntime](https://www.nuget.org/packages/NumSharp.Interop.OnnxRuntime) | 0.80.0 | Eli Belash, Haiping Chen, Mei… | Zero-copy interop between NumSharp NDArray and ONNX Runtime (Microsoft.ML.OnnxR… |
| 2026-11-08 17:05:35 | [NumSharp.Interop.System.Numerics.Tensors](https://www.nuget.org/packages/NumSharp.Interop.System.Numerics.Tensors) | 0.80.0 | Eli Belash, Haiping Chen, Mei… | Zero-copy interop between NumSharp NDArray and System.Numerics.Tensors (Tensor<… |
| 2026-11-08 17:06:48 | [Tapis.Core.Push](https://www.nuget.org/packages/Tapis.Core.Push) | 1.0.0 | Tapis Organization | Tapis.Core FCM HTTP v1 push bildirimi göndericisi (kalıcılık yok). Publicly dis… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
