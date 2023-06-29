Highcharts.getJSON('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson', function (geojson) {

    // Mapear as siglas dos estados brasileiros
    var stateCodes = {
        "Acre": "AC",
        "Alagoas": "AL",
        "Amapá": "AP",
        "Amazonas": "AM",
        "Bahia": "BA",
        "Ceará": "CE",
        "Distrito Federal": "DF",
        "Espírito Santo": "ES",
        "Goiás": "GO",
        "Maranhão": "MA",
        "Mato Grosso": "MT",
        "Mato Grosso do Sul": "MS",
        "Minas Gerais": "MG",
        "Pará": "PA",
        "Paraíba": "PB",
        "Paraná": "PR",
        "Pernambuco": "PE",
        "Piauí": "PI",
        "Rio de Janeiro": "RJ",
        "Rio Grande do Norte": "RN",
        "Rio Grande do Sul": "RS",
        "Rondônia": "RO",
        "Roraima": "RR",
        "Santa Catarina": "SC",
        "São Paulo": "SP",
        "Sergipe": "SE",
        "Tocantins": "TO"
    };

    // Mapear as siglas dos estados com os valores desejados
    var data = [
        ["AC", 1],
        ["AL", 2],
        ["AP", 3],
        ["SP", 15]
        // Adicione os demais estados e valores aqui
    ];

    // Adicionar as siglas dos estados ao GeoJSON
    for (var i = 0; i < geojson.features.length; i++) {
        var stateName = geojson.features[i].properties.name;
        var stateCode = stateCodes[stateName];
        geojson.features[i].properties.code_hasc = stateCode;
    }

    // Inicializar o gráfico Highcharts
    Highcharts.mapChart('container', {
        chart: {
            map: geojson
        },

        title: {
            text: 'GeoJSON in Highmaps'
        },

        accessibility: {
            typeDescription: 'Map of Brazil.'
        },

        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        colorAxis: {
            tickPixelInterval: 100
        },

        series: [{
            data: data,
            keys: ['code_hasc', 'value'],
            joinBy: 'code_hasc',
            name: 'Random data',
            dataLabels: {
                enabled: true,
                format: '{point.properties.postal}'
            }
        }]
    });
});
