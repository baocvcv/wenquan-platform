<template>
    <div class="multiple-choice-component">
        <v-form ref="multi-choice-form" v-model="valid">
            <v-text-field label="Title" v-model="title" outlined></v-text-field>
            <v-textarea 
                label="Content"
                v-model="content" 
                outlined
                auto-grow
            ></v-textarea>
            <v-list>
                <v-list-item-group>
                    <v-list-item
                        v-for="(item,index) in choices"
                        :key="item.name"
                    >
                        <v-list-item-icon>{{ item.name }}</v-list-item-icon>
                        <v-text-field
                            placeholder="Enter choice"
                            v-model="item.content"
                        ></v-text-field>
                        <v-btn icon small
                            @click="removeChoice(index)">
                            <v-icon>mdi-minus</v-icon>
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
        </v-form>
    </div>
</template>

<script>
export default {
    name: "multiple-choice",
    props: {

    },
    methods: {
        addChoice() {
            let length=this.choices.length;
            this.choices.push({
                name: String.fromCharCode(65+length),
                content: ""
            });
        },
        removeChoice(index) {
            this.choices.splice(index,1);
            for(var i=0;i<this.choices.length;i++)
                this.choices[i].name=String.fromCharCode(65+i);
        }
    },
    data: function() {
        return {
            valid: false,
            title: "",
            content: "",
            choices: [
                {
                    name: "A",
                    content: "",
                },
                {
                    name: "B",
                    content: "",
                },
                {
                    name: "C",
                    content: "",
                },
                {
                    name: "D",
                    content: "",
                },
            ]
        };
    }
}
</script>