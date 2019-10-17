<template>
    <div class="multiple-choice-component">
        <v-form ref="multi-choice-form" v-model="valid">
            <v-text-field label="Title" v-model="data.title" outlined></v-text-field>
            <v-textarea 
                label="Content"
                v-model="data.content" 
                :rules="[v => !!v || 'Question content is required!']"
                outlined
                auto-grow
            ></v-textarea>
            <v-list flat>
                <v-list-item-group color="primary">
                    <v-list-item
                        v-for="(item,index) in data.choices"
                        :key="item.name"
                    >
                        <v-list-item-icon>
                            {{ item.name }}
                        </v-list-item-icon>
                        <v-text-field
                            placeholder="Enter choice"
                            v-model="item.content"
                        ></v-text-field>
                        <v-btn icon small
                            @click="changeRightStatus(item)">
                            <v-icon color="green" v-if="item.right">mdi-check-circle</v-icon>
                            <v-icon color="red" v-else>mdi-close-circle</v-icon>
                        </v-btn>
                        <v-btn icon small
                            @click="removeChoice(index)">
                            <v-icon color="red">mdi-minus</v-icon>
                        </v-btn>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
            <v-btn
                class="mx-2"
                fab
                dark
                color="indigo"
                @click="addChoice()"
            >
                <v-icon dark>mdi-plus</v-icon>
            </v-btn>
            <div>
                You have chose {{ answer }}
            </div>
            <v-textarea 
                label="Analyse"
                v-model="data.analyse" 
                :rules="[v => !!v || 'Analyse is required!']"
                outlined
                auto-grow
            ></v-textarea>
                <v-btn
                    class="mr-4"
                    color="success"
                    @click="submit()"
                    :disabled="!canSubmit"
                >
                    Submit
                </v-btn>
        </v-form>
    </div>
</template>

<script>
export default {
    name: "multiple-choice",
    props: {
        data: {
            type: Object,
            default: () => {
                return {
                    title: "",
                    content: "",
                    choices: [
                        {
                            name: "A",
                            content: "",
                            right: false
                        },
                        {
                            name: "B",
                            content: "",
                            right: false
                        },
                        {
                            name: "C",
                            content: "",
                            right: false
                        },
                        {
                            name: "D",
                            content: "",
                            right: false
                        },
                    ],
                    rightAnswer: [],
                    analyse: "",
                };
            }
        }
    },
    computed: {
        answer() {
            let ans=[];
            this.data.rightAnswer.every(item => ans.push(item.name));
            if(ans.length<1) return "none";
            else return ans.join("");
        },
        canSubmit() {
            return this.valid && this.answer!="none";
        }
    },
    methods: {
        addChoice() {
            let length=this.data.choices.length;
            this.data.choices.push({
                name: String.fromCharCode(65+length),
                content: "",
                right: false
            });
        },
        removeChoice(index) {
            if(this.data.choices[index].right)
                this.data.rightAnswer.splice(this.data.rightAnswer.indexOf(this.data.choices[index]));
            this.data.choices.splice(index,1);
            for(var i=0;i<this.data.choices.length;i++)
                this.data.choices[i].name=String.fromCharCode(65+i);
        },
        changeRightStatus(item) {
            item.right=!item.right;
            if(item.right) this.data.rightAnswer.push(item);
            else this.data.rightAnswer.splice(this.data.rightAnswer.indexOf(item),1);
            this.data.rightAnswer.sort((a,b) => a.name>b.name);
            console.log(JSON.stringify(this.data.rightAnswer))
            this.$forceUpdate(); //Deal with update bug when selected > 4
        },
        submit() {
            console.log(JSON.stringify(this.data));
        },
    },
    data: function() {
        return {
            valid: false,
        };
    }
}
</script>