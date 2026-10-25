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

## Latest list — 2026-10-25 01:21 UTC

New packages created between 2026-10-25 00:21 UTC and 2026-10-25 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T01-21-18-940735Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 00:28:25 | [VQ](https://www.nuget.org/packages/VQ) | 0.0.1 | JRBlockkop, AaronoLW | C# Bindings for the VizQuick library |
| 2026-10-25 00:46:23 | [Web3TotalButton](https://www.nuget.org/packages/Web3TotalButton) | 1.0.1 | Steven-Carol | A beautiful and customizable Button control for WinUI 3 applications. |
| 2026-10-25 00:50:35 | [Nops.Core](https://www.nuget.org/packages/Nops.Core) | 1.0.0 | Nops Contributors | In-process SOPS decryption for .NET - format parsing, MAC verification, and age… |
| 2026-10-25 00:50:35 | [Nops.Configuration](https://www.nuget.org/packages/Nops.Configuration) | 1.0.0 | Nops Contributors | Microsoft.Extensions.Configuration provider for SOPS-encrypted files (YAML, JSO… |
| 2026-10-25 00:50:35 | [Nops.Core.AwsKms](https://www.nuget.org/packages/Nops.Core.AwsKms) | 1.0.0 | Nops Contributors | AWS KMS master key provider for Nops - in-process SOPS decryption. |
| 2026-10-25 00:50:35 | [Nops.Core.GcpKms](https://www.nuget.org/packages/Nops.Core.GcpKms) | 1.0.0 | Nops Contributors | GCP KMS master key provider for Nops - in-process SOPS decryption. |
| 2026-10-25 00:50:36 | [Nops.Core.Azkv](https://www.nuget.org/packages/Nops.Core.Azkv) | 1.0.0 | Nops Contributors | Azure Key Vault master key provider for Nops - in-process SOPS decryption. |
| 2026-10-25 00:50:36 | [Nops.Core.Vault](https://www.nuget.org/packages/Nops.Core.Vault) | 1.0.0 | Nops Contributors | HashiCorp Vault Transit master key provider for Nops - in-process SOPS decrypti… |
| 2026-10-25 01:09:01 | [Dloizides.Payments.Abstractions](https://www.nuget.org/packages/Dloizides.Payments.Abstractions) | 1.0.0 | DLoizides | Stripe-free merchant payment value objects (MerchantStripeCredentials, Merchant… |
| 2026-10-25 01:12:38 | [Workes.ConsoleSystem.Unity.Logging](https://www.nuget.org/packages/Workes.ConsoleSystem.Unity.Logging) | 1.0.0 | Workes | Optional Unity application log callback adapter for Workes.ConsoleSystem with N… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
