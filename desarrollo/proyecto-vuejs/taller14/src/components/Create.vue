<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="nombre">Nombre</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="estudiante.nombre"
                    v-validate="'required'"
                    name="nombre"
                    placeholder="Ingres su nombre"
                    :class="{'is-invalid': errors.has('estudiante.nombre') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="apellido">Apellido</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="estudiante.apellido"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingres su apellido"
                    :class="{'is-invalid': errors.has('estudiante.apellido') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="cedula">Edad</label>
                <input
                    type="text"
                    class="form-control"
                    id="cedula"
                    v-model="estudiante.edad"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingres su edad"
                    :class="{'is-invalid': errors.has('estudiante.edad') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid cedula.
                </div>
            </div>

            <div class="form-group">
                <label for="correo">Nacionalidad</label>
                <input
                    type="text"
                    class="form-control"
                    id="correo"
                    v-model="estudiante.nacionalidad"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingres su nacionalidad"
                    :class="{'is-invalid': errors.has('estudiante.nacionalidad') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid correo.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            estudiante: {
                nombre: '',
                apellido: '',
                edad: '',
                nacionalidad: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                console.log(this.correo)
                axios.post('http://127.0.0.1:8000/api/propietarios/',
                        this.estudiante
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>
