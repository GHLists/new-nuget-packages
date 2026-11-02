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

## Latest list — 2026-11-02 05:18 UTC

New packages created between 2026-11-02 04:20 UTC and 2026-11-02 05:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T05-18-58-080276Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 04:37:31 | [ClientPipe](https://www.nuget.org/packages/ClientPipe) | 1.0.0 | Luigi Llerena | Librería ligera para registrar clientes HTTP tipados con SocketsHttpHandler opt… |
| 2026-11-02 04:47:30 | [Kernova.Data.Sqlite](https://www.nuget.org/packages/Kernova.Data.Sqlite) | 1.0.0 | D3xSh | Acesso simples ao SQLite para aplicações .NET utilizando Dapper. |
| 2026-11-02 04:49:19 | [Softbetamx.Rfid](https://www.nuget.org/packages/Softbetamx.Rfid) | 0.1.0 | Carlos Betancourt / SOFTBETAMX | One async .NET API for UHF RFID readers: Focus (EX10/"Moduletech" protocol, Imp… |
| 2026-11-02 04:52:39 | [OpenUI.Lang.Core](https://www.nuget.org/packages/OpenUI.Lang.Core) | 1.0.0 | Dale Francis | OpenUI Lang for .NET: parser, streaming, evaluation, edit merge and system prom… |
| 2026-11-02 04:52:40 | [OpenUI.Lang.AspNetCore](https://www.nuget.org/packages/OpenUI.Lang.AspNetCore) | 1.0.0 | Dale Francis | The ASP.NET Core endpoint for the stock OpenUI react-ui chat. Streams any Micro… |
| 2026-11-02 04:58:13 | [FulcrumCore.Jev](https://www.nuget.org/packages/FulcrumCore.Jev) | 0.2.0 | Fulcrum contributors | Fulcrum provider for the native Jev System One API (POST /v1/systemone). Experi… |
| 2026-11-02 04:58:13 | [FulcrumCore.OpenAI](https://www.nuget.org/packages/FulcrumCore.OpenAI) | 0.2.0 | Fulcrum contributors | Fulcrum provider for any OpenAI-compatible chat completions endpoint (OpenAI, O… |
| 2026-11-02 04:58:14 | [FulcrumCore](https://www.nuget.org/packages/FulcrumCore) | 0.2.0 | Fulcrum contributors | Turn System One model answers into committed outcomes: typed questions, first-m… |
| 2026-11-02 05:03:22 | [ResponseResultHandler.AspNetCore.OpenApi](https://www.nuget.org/packages/ResponseResultHandler.AspNetCore.OpenApi) | 16.3.0 | Yahya Erdogan | Microsoft.AspNetCore.OpenApi integration for ResponseResultHandler: documents t… |
| 2026-11-02 05:12:12 | [Webority.Social.Sourcing](https://www.nuget.org/packages/Webority.Social.Sourcing) | 0.8.0 | Webority Technologies | Finds and picks what a brand's voices post about, for products on Webority.Soci… |
| 2026-11-02 05:12:14 | [Webority.Social.Cards](https://www.nuget.org/packages/Webority.Social.Cards) | 0.8.0 | Webority Technologies | Branded image cards for the drafts a product reviews on Webority.Social.Content… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
