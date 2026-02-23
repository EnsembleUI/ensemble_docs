import nextra from 'nextra'

const withNextra = nextra({})

export default withNextra({
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
