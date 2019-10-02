<template>
  <div>
    <TheNavbar />
    <TheSidebar />
    <nuxt id="content" />
  </div>
</template>

<script>
import TheNavbar from '~/components/TheNavbar.vue'
import TheSidebar from '~/components/TheSidebar.vue'

export default {
  components: { TheNavbar, TheSidebar }
}
</script>

<style lang="stylus" scoped>
#navbar {
  left: 0;
  z-index: 100;
  border-right: 2px solid white
  width: 102px //compensate the 2px-thick border
}

#sidebar {
  left: 100px
  width: 0
}

#content {
  width: calc(100vw - 100px);
  margin-left: 100px;
  background black
  color white
  height 100vh
  overflow hidden
}

html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}
</style>
