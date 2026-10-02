import nextra from 'nextra'
import { createRequire } from 'module';

var require = createRequire(import.meta.url);
var module = { exports: {} };

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
});
