from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dashboard, UserDashboard, PhaseContent, TrainingContent, Material
from .serializers import DashboardSerializer, UserDashboardSerializer, PhaseContentSerializer, \
    TrainingSerializer, MaterialSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DashboardView(APIView):
    permission_classes = IsAuthenticated,

    def get(self, request):
        dashboard = Dashboard.objects.first()
        if not dashboard:
            return Response({'message': 'no dashboard content'}, status=status.HTTP_404_NOT_FOUND)
        return Response(DashboardSerializer(dashboard).data)


class UserDashboardView(APIView):
    permission_classes = IsAuthenticated,

    def get(self, request):
        user_dashboard = UserDashboard.objects.get(user=request.user)
        return Response(UserDashboardSerializer(user_dashboard).data)


class PhaseView(APIView):
    permission_classes = IsAuthenticated,

    # def convert_to_dict(self, data):

    def get(self, request, phase=None):
        if not ((phase > 0) and (phase <= 3)):
            return Response({'message': 'phase not found'}, status=status.HTTP_404_NOT_FOUND)
        phase_obj = PhaseContent.objects.filter(phase='phase {}'.format(phase))
        dashboard = Dashboard.objects.first()
        serializer = PhaseContentSerializer(phase_obj, many=True)
        data = {'content': serializer.data}
        user_stats = UserDashboard.objects.get(user=request.user)
        if phase == 1:
            data.update({'progress': user_stats.phase1_progress})
            data.update({'description': dashboard.phase1_description})
            data.update({'notification': dashboard.notification})
        if phase == 2:
            data.update({'progress': user_stats.phase2_progress})
            data.update({'description': dashboard.phase2_description})
            data.update({'notification': dashboard.notification})
        if phase == 3:
            data.update({'progress': user_stats.phase3_progress})
            data.update({'description': dashboard.phase3_description})
            data.update({'notification': dashboard.notification})
        return Response(data)


class TrainingView(APIView):
    permission_classes = IsAuthenticated,

    def get(self, request):
        trainings = TrainingContent.objects.all()
        serializer = TrainingSerializer(trainings, many=True)
        dashboard = Dashboard.objects.first()
        data = {'notification': dashboard.notification, 'data': serializer.data}
        return Response(data)


class MaterialViewSet(ModelViewSet):
    permission_classes = IsAuthenticated,
    serializer_class = MaterialSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Material.objects.all()
        type_ = self.request.GET.get('type')
        if type_:
            queryset = queryset.filter(material_type=type_)
        return queryset
