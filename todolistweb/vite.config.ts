import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: 'src/app/layout.tsx' // 根据你的项目结构设置正确的入口点路径
      }
    }
  }
});