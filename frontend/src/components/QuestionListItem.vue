<template>
    <div id="question-list-item">
        <v-card>
            <v-card-title>
                <v-chip
                    v-for="tag in tags"
                    :key="tag"
                >
                    {{ tag }}
                </v-chip>
                <div class="flex-grow-1"></div>
                <v-rating
                    v-model="difficulty"
                    readonly
                    small
                    dense
                ></v-rating>
            </v-card-title>
            <v-card-text
                class="question-content" 
                ref="content"
                v-bind:style="{'max-height': max_height + 'px'}"
            >
                <span>{{ content }}</span>
                <div 
                    class="read-more" 
                    v-if="content_too_long && hide_content"
                >
                    <v-btn icon v-on:click="read_more">
                        <v-icon>mdi-chevron-down</v-icon>
                    </v-btn>
                </div>
                <div class="collapse" v-if="content_too_long && !hide_content">
                    <v-btn icon v-on:click="collapse">
                        <v-icon>mdi-chevron-up</v-icon>
                    </v-btn>
                </div>
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
export default {
    name: "question-list-item",
    props: {
        tags: Array,
        difficulty: Number,
        type: String,
        content: String,
        id: Number
    },
    data: () => ({
        hide_content: false,
        content_too_long: false,
        width: 0,
        max_height: 120,
        max_height_cache: 0
    }),
    computed: {},
    mounted() {
        window.addEventListener('resize', this.handleResize);
        this.handleResize();
        this.max_height_cache = this.max_height;
    },
    watch: {
        width: function() {
            let content = this.$refs.content;
            if (content.offsetHeight >= this.max_height)
            {
                this.content_too_long = true;
                this.hide_content = true;
            }
            else
            {
                this.content_too_long = false;
                this.hide_content = false;
            }
        }
    },
    methods: {
        handleResize() {
            this.width = window.innerWidth;
        },
        read_more() {
            this.max_height = 1000000000;
            this.hide_content = true;
        },
        collapse() {
            this.max_height = this.max_height_cache;
            this.hide_content = false;
        }
    }
}
</script>

<style scoped>
.question-content {
    overflow: hidden;
    position: relative;
}

.question-content .read-more {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    text-align: center;
    margin: 0;
    padding: 20px 0;

    background-image: linear-gradient(to bottom, transparent, white);
}

.question-content .collapse {
    position: absolute;
    bottom: 0;
    left: 0;
    text-align: center;
    margin-top: 10px;
}
</style>