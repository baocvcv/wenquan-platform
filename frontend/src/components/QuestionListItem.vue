<template>
    <div id="question-list-item">
        <v-card outlined>
            <v-card-title>
                <v-chip color="primary">
                    {{ question.question_type }}
                </v-chip>
                <!--TODO: Change here into computed-->
                <v-chip
                    v-for="tag in question.question_tags"
                    :key="tag"
                >
                    {{ tag }}
                </v-chip>
                <div class="flex-grow-1"></div>
                <v-rating
                    v-model="question.question_level"
                    readonly
                    small
                    dense
                ></v-rating>
            </v-card-title>
            <v-spacer></v-spacer>
            <v-card-text
                class="question-content" 
                ref="content"
                v-bind:style="{'max-height': max_height + 'px'}"
            >
                <v-textarea
                    outlined
                    readonly
                    label="Question"
                    v-model="question.question_content"
                >
                </v-textarea>
                <v-textarea
                    outlined
                    readonly
                    label="Answer"
                    v-model="question.question_ans"
                >
                </v-textarea>
                <div 
                    class="read-more" 
                    v-if="content_too_long && hide_content"
                >
                    <v-btn icon v-on:click="read_more">
                        <v-icon>mdi-chevron-down</v-icon>
                    </v-btn>
                </div>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <div 
                    class="collapse" 
                    v-if="content_too_long && !hide_content"
                >
                    <v-btn text v-on:click="collapse">
                        Collapse
                    </v-btn>
                </div>
            </v-card-actions>
        </v-card>
    </div>
</template>

<script>
export default {
    name: "question-list-item",
    props: {
        question: Object
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
    computed: {
        tags() {
            let tags = [];
            for (node in this.question.parents_node)
            {
                this.$axios
                    .get("/api/nodes_list/" + node + "/")
                    .then((response) => {
                        tags.push(response.data.name);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
            return tags;
        }
    },
    methods: {
        handleResize() {
            this.width = window.innerWidth;
        },
        read_more() {
            this.max_height = 1000000000;
            this.hide_content = false;
        },
        collapse() {
            this.max_height = this.max_height_cache;
            this.hide_content = true;
        },
        click() {
            this.$router.push("/admin/questions/" + this.question.id + "/");
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
    width: 100%;
    text-align: center;
}
</style>