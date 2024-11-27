import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

//bootstrap
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-icons/font/bootstrap-icons.css'


//vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader


const vuetify = createVuetify({
  components,
  directives
})

const app = createApp(App)

app.use(router)
app.use(vuetify)
app.mount('#app')
