<template>
  <div :class="pageIsClass">
    <TheNavbar />
    <TheSidebar />
    <div id="content">
      <TheBreadcrumbs />
      <nuxt />
    </div>
  </div>
</template>

<script>
import TheNavbar from '~/components/TheNavbar.vue'
import TheSidebar from '~/components/TheSidebar.vue'
import TheBreadcrumbs from '~/components/TheBreadcrumbs.vue'

export default {
  components: { TheNavbar, TheSidebar, TheBreadcrumbs },

  computed: {
    pageIsClass() {
      return `page-is-${this.$route.name}`
    }
  }
}
</script>

<style lang="stylus">
#navbar {
  left: 0;
  z-index: 100;
}

#sidebar {
  left: 100px;
  z-index: 100;
}

#content {
  width: calc(100vw - 100px - 300px);
  margin-left: 100px + 300px;
  padding: 20px;
  background: #1a1a1a
  height: 100vh;
  color: white;
}

html {
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
  background black
}

a:focus, a:active, button::-moz-focus-inner, input[type='reset']::-moz-focus-inner, input[type='button']::-moz-focus-inner, input[type='submit']::-moz-focus-inner, select::-moz-focus-inner, input[type='file'] > input[type='button']::-moz-focus-inner {
  border: 0;
  outline: 0;
}

*, *:before, *:after {
  box-sizing: border-box;
  margin: 0;
}
</style>
