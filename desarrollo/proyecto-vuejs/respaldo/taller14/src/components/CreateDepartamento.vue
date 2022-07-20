<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costo">Costo</label>
                <input
                    type="text"
                    class="form-control"
                    id="costo"
                    v-model="departamento.costo"
                    v-validate="'required'"
                    name="costo"
                    placeholder="Ingrese costo"
                    :class="{'is-invalid': errors.has('departamento.costo') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="cuartos">Número de Cuartos</label>
                <input
                    type="text"
                    class="form-control"
                    id="banios"
                    v-model="departamento.cuartos"
                    v-validate="'required'"
                    name="cuartos"
                    placeholder="Ingrese el número de cuartos"
                    :class="{'is-invalid': errors.has('departamento.cuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>
            <div class="form-group">
                <label for="banios">Número de Baños</label>
                <input
                    type="text"
                    class="form-control"
                    id="banios"
                    v-model="departamento.banios"
                    v-validate="'required'"
                    name="banios"
                    placeholder="Ingrese el número de baños"
                    :class="{'is-invalid': errors.has('departamento.banios') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>
            <div class="form-group">
                <label for="alicuota">Valor de Alícuota</label>
                <input
                    type="text"
                    class="form-control"
                    id="alicuota"
                    v-model="departamento.alicuota"
                    v-validate="'required'"
                    name="alicuota"
                    placeholder="Ingrese el valor de alícuota"
                    :class="{'is-invalid': errors.has('departamento.alicuota') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
              <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
                        </select>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                costo: '',
                cuartos: '',
                banios: '',
                alicuota: '',
                propietario: '',
            },
            propietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getPropietariosList()
    },
    methods: {
      getPropietariosList() {
            axios
            .get('http://127.0.0.1:8000/api/propietarios/')
            .then(response => {
                this.propietariosList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.post('http://127.0.0.1:8000/api/departamentos/',
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script>
