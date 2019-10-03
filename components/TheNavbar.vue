<template lang="pug">
    nav#navbar
        Logo
        ul.links
            //Order is reversed because of writing-mode: sideways-lr
            li.link(:class="currentClass('graphism')"): nuxt-link(to="/graphism") Graphism
            li.link(:class="currentClass('music')"):    nuxt-link(to="/music") Music
            li.link(:class="currentClass('software')"): nuxt-link(to="/software") Software
</template>

<script>
import Logo from '~/components/Logo.vue'

export default {
  components: {
    Logo
  },
  methods: {
    currentClass(pathFragment) {
      const currentFirstPathFragment = this.$route.path.split('/')[1]
      return { current: currentFirstPathFragment === pathFragment }
    }
  }
}
</script>

<style lang="stylus" scoped>
nav {
  background: black;
  height: 100vh;
  width: 100px;
  position: fixed;
  display: grid;
  grid-template-rows: 3fr 1fr;
}

.links {
  writing-mode: sideways-lr;
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}

.link {
  margin-top: 70px;

  &:not(:hover):not(.current) {
    opacity: 0.5;
  }
}

.link a {
  color: white;
  font-family: 'Narita Monospace';
  text-decoration: none;
  font-size: 25px;
  text-transform lowercase
}
</style>
