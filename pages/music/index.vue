<template lang="pug">
    #inner-content
        ul.items-grid
            li(v-for="file in square_cover_arts" :style="{backgroundImage: `url('${file}')`}")
</template>
