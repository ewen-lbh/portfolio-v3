<template lang="pug">
    aside#sidebar
        slot
</template>

<style lang="stylus" scoped>
#sidebar
    height 100vh
    width: 300px
    position fixed
    background #0d0d0d
    transition all 0.25s ease
</style>
