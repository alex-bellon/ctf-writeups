# cant_even_unplug_it
## Intro, Recon, Web, 102 points

### Prompt

You know, we had this up and everything. Prepped nice HTML5, started deploying on a military-grade-secrets.dev subdomain, got the certificate, the whole shabang. Boss-man got moody and wanted another name, we set up the new names and all. Finally he got scared and unplugged the server. Can you believe it? Unplugged. Like that can keep it secret…

Hint: these are HTTPS sites. Who is publicly and transparently logging the info you need?

Just in case: all info is freely accessible, no subscriptions are necessary. The names cannot really be guessed.

### Solution

The prompt mentions something about HTTPS sites, which means that the site needed to get a certificate somewhere. That means some information about the certification is probably available publicly online.

I went to [entrust.com](https://www.entrust.com/ct-search/) to search for any certificate information I could find.

I searched for `military-grade-secrets.dev` and include subdomains and expired certificates:

![](certs.png)

It showed that there were two other subdomains, `secret-storage.military-grade-secrets.dev` and `now.under.even-more-militarygrade.pw.military-grade-secrets.dev`. Plugging in either to a browser will redirect you to `forget-me-not.even-more-militarygrade.pw`, but the webpage doesn't work.

The website probably worked at some point (since it was 'unplugged'), so I went to the [Wayback Machine](https://archive.org/web/web.php) and plugged in `https://forget-me-not.even-more-militarygrade.pw/`. I clicked on the date it was first indexed, March 9th and got this webpage:

![](flag.png)

Flag: `OOO{DAMNATIO_MEMORIAE}`
