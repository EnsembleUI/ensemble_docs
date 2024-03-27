import React from 'react'
import { useRouter } from 'next/router'
import { useConfig, DocsThemeConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  useNextSeoProps() {
    const { asPath } = useRouter()
    if (asPath !== '/') {
      return {
        titleTemplate: '%s – Ensemble Docs'
      }
    }
  },
  logo: <span>Ensemble Docs</span>,
  project: {
    link: 'https://github.com/ensembleui/',
  },
  chat: {
    link: 'https://discord.gg/cEHkJTmn75',
  },
  docsRepositoryBase: 'https://github.com/EnsembleUI/ensemble_docs/blob/main',
  footer: {
    text: 'Ensemble',
  },
  sidebar: {
    defaultMenuCollapseLevel: 1
  },
  head: () => {
    const { asPath, defaultLocale, locale } = useRouter()
    const { frontMatter } = useConfig()
    const url =
      'https://ensembleui.com' +
      (defaultLocale === locale ? asPath : `/${locale}${asPath}`)
 
    return (
      <>
        <meta property="og:url" content={url} />
        <meta property="og:title" content={frontMatter.title || 'Ensemble'} />
        <meta
          property="og:description"
          content={frontMatter.description || 'Ensemble Docs'}
        />
      </>
    )
  }
}

export default config
