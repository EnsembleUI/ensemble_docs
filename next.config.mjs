import nextra from 'nextra'

const withNextra = nextra({})

export default withNextra({
  output: 'export',
  images: { unoptimized: true },
  async redirects() {
    return [
      {
        source: '/error/:errorId',
        destination: '/tips-and-tricks/:errorId',
        permanent: false,
      },
      {
        source: '/doc/:topic',
        destination: '/concepts/:topic',
        permanent: false,
      },
    ]
  },
})
