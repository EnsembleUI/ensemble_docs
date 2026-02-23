import { Footer, Layout, Navbar } from 'nextra-theme-docs'
import { Head } from 'nextra/components'
import { getPageMap } from 'nextra/page-map'
import 'nextra-theme-docs/style.css'

export const metadata = {
  title: {
    template: '%s – Ensemble Docs',
    default: 'Ensemble Docs',
  },
  description: 'Ensemble Docs',
  openGraph: {
    url: 'https://ensembleui.com',
    title: 'Ensemble',
    description: 'Ensemble Docs',
    siteName: 'Ensemble Docs',
  },
}

const navbar = (
  <Navbar
    logo={<span>Ensemble Docs</span>}
    projectLink="https://github.com/ensembleui/"
    chatLink="https://discord.gg/cEHkJTmn75"
  />
)

const footer = <Footer>Ensemble</Footer>

export default async function RootLayout({ children }) {
  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head />
      <body>
        <Layout
          navbar={navbar}
          pageMap={await getPageMap()}
          docsRepositoryBase="https://github.com/EnsembleUI/ensemble_docs/blob/main"
          footer={footer}
          sidebar={{
            defaultMenuCollapseLevel: 1,
          }}
        >
          {children}
        </Layout>
      </body>
    </html>
  )
}
