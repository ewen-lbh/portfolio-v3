<template lang="pug">
    nav#navbar
        Logo
        ul.links
            //Order is reversed because of writing-mode: sideways-lr
            li.link: nuxt-link(to="/graphism") Graphism
            li.link: nuxt-link(to="/music") Music
            li.link: nuxt-link(to="/software") Software
</template>

<script lang="coffee">
import Logo from '~/components/Logo.vue'

export default {
    components: {
        Logo,
    }
}
</script>

<style lang="stylus" scoped>
nav {
    background: black;
    height 100vh
    width: 100px
    position fixed
    display grid
    grid-template-rows 3fr 1fr
}

.links {
    writing-mode: sideways-lr;
    display flex
    width 100%
    justify-content center
    align-items center
}

.link {
    margin-top: 50px
}

.link a {
    color: white;
    font-family: 'Narita Monospace';
    text-decoration none
    font-size: 30px
}
</style>
