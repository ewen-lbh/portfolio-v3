<template lang="pug">
  //-FIXME: duplicated code @ li.breadcrumb-arrow
  ul.breadcrumbs(v-if="pathFragments.length >= 1")
    li.breadcrumb-link
      nuxt-link(to="/"): i.material-icons home
    li.breadcrumb-arrow(v-if="!isLastPathFragment(pathFragment)")
      i.material-icons chevron_right

    template(v-for="pathFragment in pathFragments")  
      li.breadcrumb-link
        nuxt-link(:to="getPathFromPathFragment(pathFragment)") {{pathFragment}}
      li.breadcrumb-arrow(v-if="!isLastPathFragment(pathFragment)")
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

      return this.pathFragments
        .slice(1, pathFragmentIdx + 1)
        .map((f) => f.toLowerCase())
        .join('/')
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
  opacity: 0.25
}

.breadcrumb-link a {
  opacity: 0.5
  text-decoration: none;
  color: inherit;
  font-family: 'Product Sans';
  text-transform: uppercase;
  font-weight: bold;
  letter-spacing: 1px;
}

.breadcrumb-link:hover a {
  opacity: 1
}
</style>
