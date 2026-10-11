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

## Latest list — 2026-10-11 09:21 UTC

New packages created between 2026-10-11 08:22 UTC and 2026-10-11 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T09-21-08-296668Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 08:31:07 | [PulseSharp.Sqlite](https://www.nuget.org/packages/PulseSharp.Sqlite) | 0.3.0-alpha | Waqas Ahmad | SQLite store for PulseSharp: durable events and jobs for desktop, mobile and sm… |
| 2026-10-11 08:35:42 | [Kusachius.View2Pdf](https://www.nuget.org/packages/Kusachius.View2Pdf) | 1.4.0 | Aldis Arust | Razor view rendering and HTML-to-PDF conversion services for ASP.NET Core appli… |
| 2026-10-11 08:40:50 | [Tai.Wallet.Voucher.Domain](https://www.nuget.org/packages/Tai.Wallet.Voucher.Domain) | 0.1.0 | Tai | ABP module that redeems voucher codes and prepaid cards into Tai.Wallet balances |
| 2026-10-11 08:40:50 | [Tai.Wallet.Voucher.Application.Contracts](https://www.nuget.org/packages/Tai.Wallet.Voucher.Application.Contracts) | 0.1.0 | Tai | ABP module that redeems voucher codes and prepaid cards into Tai.Wallet balances |
| 2026-10-11 08:40:51 | [Tai.Wallet.Voucher.EntityFrameworkCore](https://www.nuget.org/packages/Tai.Wallet.Voucher.EntityFrameworkCore) | 0.1.0 | Tai | ABP module that redeems voucher codes and prepaid cards into Tai.Wallet balances |
| 2026-10-11 08:40:52 | [Tai.Wallet.Voucher.Application](https://www.nuget.org/packages/Tai.Wallet.Voucher.Application) | 0.1.0 | Tai | ABP module that redeems voucher codes and prepaid cards into Tai.Wallet balances |
| 2026-10-11 08:40:52 | [Tai.Wallet.Voucher.HttpApi](https://www.nuget.org/packages/Tai.Wallet.Voucher.HttpApi) | 0.1.0 | Tai | ABP module that redeems voucher codes and prepaid cards into Tai.Wallet balances |
| 2026-10-11 08:40:53 | [Tai.Wallet.Voucher.Domain.Shared](https://www.nuget.org/packages/Tai.Wallet.Voucher.Domain.Shared) | 0.1.0 | Tai | ABP module that redeems voucher codes and prepaid cards into Tai.Wallet balances |
| 2026-10-11 08:41:22 | [PromptPack](https://www.nuget.org/packages/PromptPack) | 1.1.0-preview-0003 | Your Name | AI-friendly repository context packer for .NET |
| 2026-10-11 08:57:01 | [Umbraco.Community.UmbraDesktop.Accessories](https://www.nuget.org/packages/Umbraco.Community.UmbraDesktop.Accessories) | 17.3.0 | Luuk Peters | The small tools for UmbraDesktop. An optional add-on that puts Notepad, Paint,… |
| 2026-10-11 09:00:37 | [Kusachius.PagingResponses](https://www.nuget.org/packages/Kusachius.PagingResponses) | 1.4.0 | Aldis Arust | Paging, sorting, and filtering helpers for ASP.NET Core and Entity Framework Co… |
| 2026-10-11 09:06:25 | [TouchSocketPro.S7](https://www.nuget.org/packages/TouchSocketPro.S7) | 4.3.10 | 若汝棋茗 | TouchSocketPro.S7 provides a native TouchSocket-style S7comm client over ISO-on… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
