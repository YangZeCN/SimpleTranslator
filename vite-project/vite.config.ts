import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default ({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');

  return  defineConfig({
    plugins: [vue()],
    server:{
      host: '0.0.0.0',
      allowHosts: true,
      proxy:{
        //将以/api开头的请求代理到目标服务器
        '/api': {
          target: env.VITE_FLASK_URL,
          changeOrigin: true,
          // rewrite:(path) => path.replace(/^\/api/,'')
        }
      }
    },
    define: {
      __LOCUST_URL__: JSON.stringify(env.VITE_LOCUST_URL),
      __FLASK_URL__: JSON.stringify(env.VITE_FLASK_URL),
    }
  })
}

