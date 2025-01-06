// deno-lint-ignore-file
const filePath = 'C:\\Users\\sejbo\\Documents\\Applications de supervision\\data.json';

try {
    // Lire le contenu du fichier JSON
    const jsonData = Deno.readTextFileSync(filePath);

    // Analyser le contenu JSON en un objet JavaScript
    const { visitors, events } = JSON.parse(jsonData);

    // Fonction pour obtenir les données des visiteurs
    function getVisitors() {
        return visitors;
    }

    // Fonction pour obtenir les données des événements
    function getEvents() {
        return events;
    }


    // Affichage des données
    // const visitorsData = getVisitors();
    // const eventsData = getEvents();

    // console.log('Données des visiteurs :', visitorsData);
    // console.log('Données des événements :', eventsData);

    // Question 2.a:
    function getMinMaxEventTime() {
        let minTime = Number.MAX_SAFE_INTEGER;
        let maxTime = Number.MIN_SAFE_INTEGER;

        for (const event of events) {
            const eventTimeParts = event.time.split(':');
            const eventHour = parseInt(eventTimeParts[0], 10);
            const eventMinute = parseInt(eventTimeParts[1], 10);

            const eventTotalMinutes = eventHour * 60 + eventMinute;

            if (eventTotalMinutes < minTime) {
                minTime = eventTotalMinutes;
            }

            if (eventTotalMinutes > maxTime) {
                maxTime = eventTotalMinutes;
            }
        }

        const minHours = Math.floor(minTime / 60);
        const minMinutes = minTime % 60;
        const maxHours = Math.floor(maxTime / 60);
        const maxMinutes = maxTime % 60;

        const minTimeFormatted = `${minHours}:${minMinutes.toString().padStart(2, '0')}`;
        const maxTimeFormatted = `${maxHours}:${maxMinutes.toString().padStart(2, '0')}`;

        return { minTime: minTimeFormatted, maxTime: maxTimeFormatted };
    }

    const { minTime, maxTime } = getMinMaxEventTime();
    console.log("2.a: Heures d'ouverture :", minTime, "@",maxTime);

    // Question 2.b:
    function getTotalVisitorCount() {
        const uniqueVisitorIds = new Set<number>();

        for (const event of events) {
            uniqueVisitorIds.add(event.visitorId);
        }

        return uniqueVisitorIds.size;
    }

    const totalVisitorCount = getTotalVisitorCount();
    console.log('2.b: Nombre total de visiteurs :', totalVisitorCount);

    // Question 3.a:
    function getVisitorCountForRoom3() {
        const uniqueVisitorIds = new Set<number>();

        for (const event of events) {
            if (event.roomId === 3) {
                uniqueVisitorIds.add(event.visitorId);
            }
        }

        return uniqueVisitorIds.size;
    }

    const visitorCountForRoom3 = getVisitorCountForRoom3();
    console.log('3.a: Nombre de visiteurs pour la salle 3 :', visitorCountForRoom3);

    // Question 3.b:
    // Fonction pour obtenir les noms des visiteurs uniques de la salle 3
    function getUniqueVisitorNamesForRoom3() {
        const uniqueVisitorIds = new Set<number>();
        const uniqueVisitorNames = new Set<string>();

        for (const event of events) {
            if (event.roomId === 3) {
                uniqueVisitorIds.add(event.visitorId);
            }
        }

        for (const visitor of visitors) {
            if (uniqueVisitorIds.has(visitor.id)) {
                uniqueVisitorNames.add(visitor.name);
            }
        }

        return Array.from(uniqueVisitorNames);
    }

    const uniqueVisitorNamesForRoom3 = getUniqueVisitorNamesForRoom3();
    // console.log("3.b: Noms des visiteurs uniques pour la chambre 3 :", uniqueVisitorNamesForRoom3);

    // Question 3.c:
    function getMostAndLeastPopularRooms() {
        const roomCounts = new Map<number, number>();

        for (const event of events) {
            const roomId = event.roomId;
            if (roomCounts.has(roomId)) {
                roomCounts.set(roomId, roomCounts.get(roomId) + 1);
            } else {
                roomCounts.set(roomId, 1);
            }
        }

        let mostPopularRoom: number | null = null;
        let leastPopularRoom: number | null = null;
        let maxCount = 0;
        let minCount = Number.MAX_SAFE_INTEGER;

        for (const [roomId, count] of roomCounts) {
            if (count > maxCount) {
                mostPopularRoom = roomId;
                maxCount = count;
            }
            if (count < minCount) {
                leastPopularRoom = roomId;
                minCount = count;
            }
        }

        return { mostPopularRoom, leastPopularRoom };
    }

    const { mostPopularRoom, leastPopularRoom } = getMostAndLeastPopularRooms();
    console.log("3.c: Salle la plus populaire :", mostPopularRoom, " Salle la moins populaire :", leastPopularRoom);

    // Question 4.a:
    // Fonction pour retracer le trajet de Jessica Daniel
    function getJessicaDanielsRoute() {
        const jessicaDanielsRoute: number[] = [];
        const jessicaDanielId = visitors.find((visitor) => visitor.name === 'Jessica Daniel')?.id;

        if (!jessicaDanielId) {
            return jessicaDanielsRoute;
        }

        for (const event of events) {
            if (event.visitorId === jessicaDanielId) {
                jessicaDanielsRoute.push(event.roomId);
            }
        }

        return jessicaDanielsRoute;
    }

    const jessicaDanielsRoute = getJessicaDanielsRoute();
    console.log('4.a: Trajet de Jessica Daniel :', jessicaDanielsRoute);

    // Question 4.b:
    function getAverageVisitsAndTime() {
        const visitorData = new Map<number, { visitedRooms: Set<number>; totalVisitTime: number }>();

        for (const event of events) {
            const visitorId = event.visitorId;
            const roomId = event.roomId;

            if (!visitorData.has(visitorId)) {
                visitorData.set(visitorId, {
                    visitedRooms: new Set<number>(),
                    totalVisitTime: 0,
                });
            }

            const visitorInfo = visitorData.get(visitorId);
            if (visitorInfo) {
                visitorInfo.visitedRooms.add(roomId);
            }
        }

        let totalRoomsVisited = 0;

        for (let { visitedRooms} of visitorData.values()) {
            totalRoomsVisited += visitedRooms.size;
        }

        const averageRoomsVisited = Math.round(totalRoomsVisited / visitorData.size);   // Arrondir à l'entier près

        return {averageRoomsVisited};
    }

    const { averageRoomsVisited, averageVisitTime } = getAverageVisitsAndTime();
    console.log('4.b: Moyenne du nombre de salles visitées par visiteur :', averageRoomsVisited);

    // Question 4.c:
    // Créer un objet pour compter le nombre de salles visitées par chaque visiteur
    const visitorRoomCounts = new Map<number, number>();

    // Parcourir les événements pour compter les salles visitées par chaque visiteur
    for (const event of events) {
        const visitorId = event.visitorId;
        visitorRoomCounts.set(visitorId, (visitorRoomCounts.get(visitorId) || 0) + 1);
    }

    // Trouver le visiteur ayant visité le plus de salles
    const [maxVisitorId, maxRoomCount] = [...visitorRoomCounts.entries()].reduce((prev, curr) => curr[1] > prev[1] ? curr : prev);

    const mostVisitedVisitor = visitors.find((visitor) => visitor.id === maxVisitorId);
    console.log('4.c: Nom du visiteur ayant visité le plus de salles :', mostVisitedVisitor.name);

    // Question 5.a et question 5.b:
    console.log("5.a: n/a\n5.b: n/a")
    // Je n'ai pas pu déterminer le programme me permettant de trouver l'entrée du musée, mais par le tri des événements,
    // Je vais estimer que l'entrée est représentée par la salle 7 et les sorties par la salle 7 et 10.

    // Question 5.c:
    function isRoom5AdjacentTo8Or9() {
        for (let i = 0; i < events.length - 1; i++) {
            const currentEvent = events[i];
            const nextEvent = events[i + 1];

            // Vérifier si un visiteur est passé de la salle 5 à la salle 8 ou 9
            if (
                currentEvent.roomId === 5 &&
                (nextEvent.roomId === 8 || nextEvent.roomId === 9)
            ) {
                return true;
            }
        }

        return false;
    }

    const isAdjacent = isRoom5AdjacentTo8Or9();

    if (isAdjacent) {
        console.log("5.c: Au moins un visiteur est passé de la salle 5 à la salle 8 ou 9.");
    } else {
        console.log("5.c: Aucun visiteur n'est passé de la salle 5 à la salle 8 ou 9.");
    }

} catch (error) {
    console.error(`Erreur lors de la lecture ou du parsing du fichier JSON : ${error}`);
}
