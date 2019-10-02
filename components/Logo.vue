<template lang="pug">
    nuxt-link(:to="navigateTo")
        img(src="~/assets/images/logos/Mx3 Favicon Light.png")
</template>

<script lang="coffee">
export default {
    props: {
        navigateTo: {
            type: [Boolean, String],
            default: '/',
        }
    }
}
</script>

<style lang="stylus" scoped>
img
    width 100%
    padding 30px
</style>
