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

## Latest list — 2026-11-22 23:20 UTC

New packages created between 2026-11-22 22:20 UTC and 2026-11-22 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T23-20-23-206645Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 22:27:00 | [OpenMoca.Reader.Age](https://www.nuget.org/packages/OpenMoca.Reader.Age) | 0.7.0 | MOCA Standard Contributors | Open encrypted MOCA packages: decrypt-only age v1 (X25519 and scrypt recipients… |
| 2026-11-22 22:27:37 | [Rakomi](https://www.nuget.org/packages/Rakomi) | 0.1.0 | Rakomi | OpenID Connect discovery for Rakomi: fetches and validates the provider metadat… |
| 2026-11-22 22:27:38 | [Rakomi.Sdk](https://www.nuget.org/packages/Rakomi.Sdk) | 0.1.0 | Rakomi | The Rakomi SDK for .NET. This early release brings in the Rakomi package (OpenI… |
| 2026-11-22 22:28:06 | [Blazix.Icons](https://www.nuget.org/packages/Blazix.Icons) | 0.3.0 | Halden Collier | The Icon component for Blazix's icon set packages (Blazix.Icons.Lucide, .Tabler… |
| 2026-11-22 22:28:08 | [Blazix.Icons.Lucide](https://www.nuget.org/packages/Blazix.Icons.Lucide) | 0.3.0 | Halden Collier | Lucide for Blazor: 2,400 icons as inline SVG, for Blazix.Icons' Icon component.… |
| 2026-11-22 22:28:10 | [Blazix.Icons.Tabler](https://www.nuget.org/packages/Blazix.Icons.Tabler) | 0.3.0 | Halden Collier | Tabler Icons for Blazor: 6,500 icons as inline SVG, for Blazix.Icons' Icon comp… |
| 2026-11-22 22:28:12 | [Blazix.Icons.Hugeicons](https://www.nuget.org/packages/Blazix.Icons.Hugeicons) | 0.3.0 | Halden Collier | Hugeicons for Blazor: 6,100 icons as inline SVG, for Blazix.Icons' Icon compone… |
| 2026-11-22 22:28:15 | [Blazix.Icons.Phosphor](https://www.nuget.org/packages/Blazix.Icons.Phosphor) | 0.3.0 | Halden Collier | Phosphor Icons for Blazor: 9,000 icons as inline SVG, for Blazix.Icons' Icon co… |
| 2026-11-22 22:28:17 | [Blazix.Icons.Remixicon](https://www.nuget.org/packages/Blazix.Icons.Remixicon) | 0.3.0 | Halden Collier | Remix Icon for Blazor: 3,100 icons as inline SVG, for Blazix.Icons' Icon compon… |
| 2026-11-22 22:28:19 | [Blazix.Icons.FontAwesome](https://www.nuget.org/packages/Blazix.Icons.FontAwesome) | 0.3.0 | Halden Collier | Font Awesome Free for Blazor: 2,800 icons as inline SVG, for Blazix.Icons' Icon… |
| 2026-11-22 22:32:43 | [Eternet.AspNetCore.ServiceFabric.EntityFrameworkCore](https://www.nuget.org/packages/Eternet.AspNetCore.ServiceFabric.EntityFrameworkCore) | 1.0.2 | Eternet.AspNetCore.ServiceFab… | Service Fabric readiness for Entity Framework contexts: each context must conne… |
| 2026-11-22 22:57:27 | [PoeFilterX](https://www.nuget.org/packages/PoeFilterX) | 3.30.1 | SteffenBlake | Compiler and language server for PoeFilterX filters and filter stylesheets. |
| 2026-11-22 23:02:02 | [Freenaute.Freebox.Mcp](https://www.nuget.org/packages/Freenaute.Freebox.Mcp) | 1.0.0 | Freenaute | Local stdio MCP server for read-only Freebox discovery, pairing coordination, a… |
| 2026-11-22 23:02:42 | [Lab5Package.Mku2026](https://www.nuget.org/packages/Lab5Package.Mku2026) | 1.0.0 | PavelShanygin | Package Description |
| 2026-11-22 23:11:40 | [QrDown.Uploader](https://www.nuget.org/packages/QrDown.Uploader) | 1.0.0 | QrDown.Sender | QrDown göndericisi: dosyayı animasyonlu QR dizisi olarak gösterir. Çalıştırıcı… |
| 2026-11-22 23:12:08 | [Nethouse.DocuComposer.Client](https://www.nuget.org/packages/Nethouse.DocuComposer.Client) | 1.0.0 | Nethouse Consulting | Typed .NET client for generating consistent, template-driven documents from app… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
