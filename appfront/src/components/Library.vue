<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul>
      <li v-for="item in list">
        {{ item.title}}
      </li>

    </ul>
  </div>
</template>

<script>

  export default {
    name: 'Library',
    data() {
      return {
        msg: 'this is library',
        list: [
          {
            'title': '《钢铁是怎么炼成的》',
          },
          {
            'title': '《孙子兵法》'
          },
          {
            'title': '《鲁宾逊漂流记》'
          }
        ]
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
