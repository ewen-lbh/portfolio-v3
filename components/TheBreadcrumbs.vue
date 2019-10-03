<template lang="pug">
  ul.breadcrumbs(v-if="pathFragments.length >= 1")
    li.breadcrumb-link
      nuxt-link(to="/"): i.material-icons home
    li.breadcrumb-arrow
      i.material-icons chevron_right

    template(v-for="(pathFragment, i) in pathFragments")  
      li.breadcrumb-link
        nuxt-link(v-if="i !== pathFragments.length - 1" :to="getPathFromPathFragment(pathFragment)") {{pathFragment}}
        span(v-else) {{pathFragment.replace(/-/g, ' ')}}
      li.breadcrumb-arrow(v-if="i !== pathFragments.length - 1")
        i.material-icons chevron_right
</template>

<script>
export default {
  computed: {
    pathFragments() {
      return this.$route.path.split('/').filter((f) => f.length > 0)
    }
  },
  methods: {
    isLastPathFragment(pathFragment) {
      return (
        this.pathFragments.indexOf(pathFragment) + 1 >=
        this.pathFragments.length
      )
    },
    getPathFromPathFragment(pathFragment) {
      const pathFragmentIdx = this.pathFragments.indexOf(pathFragment)
      if (pathFragmentIdx === -1) return '/'

      return (
        '/' +
        this.pathFragments
          .slice(0, pathFragmentIdx + 1)
          .map((f) => f.toLowerCase())
          .join('/')
      )
    }
  }
}
</script>

<style lang="stylus" scoped>
.breadcrumbs {
  display: flex;
  margin-left: -20px;
  align-items: center;
}

.breadcrumbs li {
  list-style: none;
  margin-right: 10px;
}

.breadcrumb-link a, .breadcrumb-arrow {
  height: 24px;
  display: flex;
  align-items: center;
}

.breadcrumb-arrow {
  opacity: 0.25;
}

.breadcrumb-link > * {
  opacity: 0.5;
  text-decoration: none;
  color: inherit;
  font-family: 'Product Sans';
  text-transform: uppercase;
  font-weight: bold;
  letter-spacing: 1px;
}

.breadcrumb-link:hover a {
  opacity: 1;
}
</style>
