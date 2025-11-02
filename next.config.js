const nextraRaw = require('nextra');
const nextra = typeof nextraRaw === 'function' ? nextraRaw : nextraRaw.default || nextraRaw;

const withNextra = nextra({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.tsx'
});

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
