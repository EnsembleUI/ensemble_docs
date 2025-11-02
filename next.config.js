const nextraModule = require('nextra')
// Handle both default export and named export cases
const nextra = typeof nextraModule === 'function' 
  ? nextraModule 
  : (nextraModule.default || nextraModule)
  
const withNextra = nextra({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.tsx'
})

module.exports = withNextra({
  async redirects() {
    return [
      {
        // from 'error/message' to 'tips-and-tricks/error-message'
        source: '/error/:errorId',
        destination: '/tips-and-tricks/:errorId',
        permanent: false,
      },
      {
        // from 'doc/:topic' to 'concepts/:topic'
        source: '/doc/:topic',
        destination: '/concepts/:topic',
        permanent: false,
      }
    ]
  }
})
