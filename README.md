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

## Latest list — 2026-11-05 15:19 UTC

New packages created between 2026-11-05 14:21 UTC and 2026-11-05 15:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T15-19-29-810441Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 14:26:22 | [FetchXmlLinter.XrmToolBox](https://www.nuget.org/packages/FetchXmlLinter.XrmToolBox) | 0.1.0 | jaduplesms | Read-only FetchXML analysis for Microsoft Dataverse in XrmToolBox. Review suppl… |
| 2026-11-05 14:49:06 | [Bijou64](https://www.nuget.org/packages/Bijou64) | 1.0.0 | iainb | Bijective variable-length encoding for unsigned integers |
| 2026-11-05 14:54:04 | [LanguageWire.Connectors.Sitecore](https://www.nuget.org/packages/LanguageWire.Connectors.Sitecore) | 5.4.2 | LanguageWire | description |
| 2026-11-05 14:59:51 | [Shiny.Hosting.Avalonia](https://www.nuget.org/packages/Shiny.Hosting.Avalonia) | 6.5.2 | Allan Ritchie | Shiny hosting for Avalonia - starts Shiny from the AppBuilder and forwards Andr… |
| 2026-11-05 14:59:52 | [Shiny.Hosting.Uno](https://www.nuget.org/packages/Shiny.Hosting.Uno) | 6.5.2 | Allan Ritchie | Shiny hosting for Uno Platform - runs Shiny inside the Uno.Extensions.Hosting c… |
| 2026-11-05 14:59:54 | [Shiny.Hosting.Uno.WebAssembly](https://www.nuget.org/packages/Shiny.Hosting.Uno.WebAssembly) | 6.5.2 | Allan Ritchie | Shiny hosting for Uno Platform WebAssembly - the IJSRuntime that Shiny's browse… |
| 2026-11-05 15:05:32 | [Telerik.AspNetCore.Templates](https://www.nuget.org/packages/Telerik.AspNetCore.Templates) | 1.0.0 | Progress Software Corporation | Telerik UI for ASP.NET Core project templates |
| 2026-11-05 15:07:16 | [RecursiveAI.OneMail.Client](https://www.nuget.org/packages/RecursiveAI.OneMail.Client) | 1.0.0 | Recursive AI, LLC | SMTP, IMAP and POP3 clients and SASL for .NET, over a public raw protocol layer. |
| 2026-11-05 15:07:17 | [RecursiveAI.OneMail.Calendar](https://www.nuget.org/packages/RecursiveAI.OneMail.Calendar) | 1.0.0 | Recursive AI, LLC | iCalendar (ICS) and vCard components, recurrence expansion and time zones for .… |
| 2026-11-05 15:07:17 | [RecursiveAI.OneMail.Render](https://www.nuget.org/packages/RecursiveAI.OneMail.Render) | 1.0.0 | Recursive AI, LLC | Renders an email message to a tagged PDF or PNG pages in one call, on OneRender… |
| 2026-11-05 15:07:18 | [RecursiveAI.OneMail.Cli](https://www.nuget.org/packages/RecursiveAI.OneMail.Cli) | 1.0.0 | Recursive AI, LLC | The onemail command-line tool: inspect, convert, recover and export email files… |
| 2026-11-05 15:07:18 | [RecursiveAI.OneMail](https://www.nuget.org/packages/RecursiveAI.OneMail) | 1.0.0 | Recursive AI, LLC | Reads and writes email formats for .NET: MIME/EML, MBOX, Maildir, TNEF, MSG, PS… |
| 2026-11-05 15:07:53 | [Kane.Extension.Full](https://www.nuget.org/packages/Kane.Extension.Full) | 3.0.0 | Kane Leung | 包含常用的反射相关基本扩展，些包包含Kane.Extension所有功能，具体请看源码 |
| 2026-11-05 15:08:44 | [Novatech.ACL.Service.Reporting](https://www.nuget.org/packages/Novatech.ACL.Service.Reporting) | 1.0.0 | Novatech | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
